import os
import re
import csv
import itertools
import subprocess

from helpers.constants import RANK, COLORS


class WikiTree:
    def __init__(self, label, rank, name=None):
        self.label = label
        self.rank = rank
        self.name = name

        self.parent = None
        self.children = set()
        if self.parent:
            self.parent.add_child(self)

        self.is_cached = False

    def __str__(self):
        string = f"{self.rank}: {self.label}"
        if self.name:
            string += f" ({self.name})"
        return string

    def __lt__(self, other):
        return (
            (-self.get_num_children(), str(self)) <
            (-other.get_num_children(), str(other))
        )

    def __dict__(self):
        return {self.label: [c.__dict__() for c in self.children]}

    def __list__(self):
        # print([(k, v) for k, v in self.get_parents()])
        dict_ = {k: v for k, v in self.get_parents()}
        dict_["Rank"] = self.rank
        if self.name:
            dict_["Common Name"] = self.name

        array = [dict_]
        for child in self.sorted_children:
            array += child.__list__()
        return array

    @property
    def sorted_children(self):
        if not self.is_cached:
            self._sorted_children = sorted(self.children)
            self.is_cached = True
        return self._sorted_children

    def add_child(self, child):
        self.children.add(child)
        self.is_cached = False

    def remove_child(self, child):
        self.children.remove(child)
        self.is_cached = False

    def get_parents(self):
        tup = (self.rank, self.label)
        if self.parent is None:
            return [tup]
        return self.parent.get_parents() + [tup]

    def get_num_children(self):
        num = len(self.children)
        num += sum(map(WikiTree.get_num_children, self.children))
        return num

    def prune(self, rank, includes):
        has_rank = 0
        for child in list(self.children):
            if child.rank == rank:
                if not includes.search(str(child)):
                    self.children.remove(child)
                else:
                    has_rank += 1
            else:
                has_rank += child.prune(rank, includes)

        if has_rank == 0:
            if self.parent:
                self.parent.children.remove(self)
        return has_rank

    def from_pov(self, from_node):
        path = iter(self.path_to_root(from_node))

        root = next(path)
        prev = root

        for node in path:
            prev.children = [*prev.children, node]
            prev = node

        return root

    def path_to(self, from_node, to_node):
        path = self.from_pov(to_node).path_to_root(from_node)
        return [n.label for n in path]

    def exclude_child(self, child):
        new_children = [x for x in self.children if x.label != child.label]
        return WikiTree(self.label, new_children)

    def path_to_root(self, from_node):
        path = self.recursive_rooter(from_node)
        if not path:
            raise ValueError(f"Node {from_node} not found")
        return path

    def recursive_rooter(self, from_node):
        print(self.label)
        if self.label == from_node:
            return [self]
        for child in self.children:
            response = child.recursive_rooter(from_node)
            if response:
                return response + [self.exclude_child(child)]

    def pretty_str(self, fix="", child_fix="", length=2, with_color=False):
        ordinal = self.sorted_children

        if with_color:
            string = "".join((
                COLORS["white"], fix, COLORS["blue"], self.rank,
                COLORS["white"], " : ", COLORS["br_green"], self.label
            ))
        else:
            string = "".join((fix, self.rank, " : ", self.label))

        if self.name:
            string += f" ({self.name})"
        string += "\n"

        if ordinal:
            for child in ordinal[:-1]:
                string += child.pretty_str(
                    child_fix + f"├{'─' * length} ",
                    child_fix + f"│{' ' * length} ",
                    length, with_color
                )
            string += ordinal[-1].pretty_str(
                child_fix + f"└{'─' * length} ",
                child_fix + f" {' ' * length} ",
                length, with_color
            )

        if fix == "" and with_color:
            string += COLORS["reset"]

        return string

    def to_txt(self, filename=None, with_color=False):
        if filename is None:
            filename = f"{self.rank}_{self.label}.txt"
        with open(filename, "w") as f:
            f.write(self.pretty_str(with_color=with_color))
        return filename

    def view(self, with_color=False):
        filename = self.to_txt(with_color=with_color)
        subprocess.run(["less", "-R", filename])
        subprocess.run(["rm", filename])

    def search(self, term, case_insensitive=False, all_results=True):
        if case_insensitive:
            pattern = re.compile(term, re.IGNORECASE)
        else:
            pattern = re.compile(term)

        try:
            filename = self.to_txt()
            with open(filename) as f:
                for index, line in enumerate(f):
                    if pattern.search(line):
                        subprocess.run(
                            ["less", f"+{index}g", "-N", "-R", filename])
                        if not all_results:
                            return
        except KeyboardInterrupt:
            pass
            # subprocess.run(["clear"])

    def to_csv(self, filename):
        lines = self.__list__()
        all_keys = sorted(
            set(key for line in lines for key in line.keys()),
            key=RANK.index
        )

        with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerow(all_keys)
            writer.writerows(
                [line[key] if key in line else "" for key in all_keys]
                for line in lines
            )

    @staticmethod
    def connect(child, parent):
        if isinstance(child, WikiTree) and isinstance(parent, WikiTree):
            to_change = False
            if not child.parent:
                to_change = True
            elif child.parent is not parent:
                prev = RANK.index(child.parent.rank)
                curr = RANK.index(parent.rank)
                if curr > prev:
                    child.parent.remove_child(child)
                    to_change = True

            if to_change:
                child.parent = parent
                parent.add_child(child)
        else:
            raise ValueError("child and parent must be WikiTree")

    @staticmethod
    def from_csv(filename):
        nodes = {}

        with open(filename) as f:
            reader = csv.DictReader(f)
            for line in reader:
                filtrate = itertools.compress(line.items(), line.values())

                rank = next(filtrate)[1]
                common_name = next(filtrate)[1]

                parent_key = None
                for child_key in filtrate:
                    # add child not if not in nodes
                    if child_key not in nodes:
                        rank, label = child_key
                        node = WikiTree(label, rank)
                        nodes[child_key] = WikiTree(label, rank)

                    # link child to parent
                    if parent_key in nodes:
                        WikiTree.connect(nodes[child_key], nodes[parent_key])

                    # copy current key to previous key
                    parent_key = child_key

                # add common name to last node
                label = nodes[child_key].label
                if not label.endswith(common_name.split()[-1]):
                    nodes[child_key].name = common_name

        any_key = next(iter(nodes.keys()))
        root_key = nodes[any_key].get_parents()[0]
        root = nodes[root_key]

        return root
