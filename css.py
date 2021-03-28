CSS = """
/* Credits */

/* Ilya Pestov: Original, https://codepen.io/Pestov/pen/BLpgm */
/* Paul Smirnov: Horizontal, https://codepen.io/paulsmirnov/pen/dyyOLwa */
/* Shane Drabing: Added some image hover effects */

/* Now the CSS */

* {
    margin: 0;
    padding: 0;
}

.tree {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-pack: start;
    -ms-flex-pack: start;
    justify-content: flex-start;
}

.tree ul {
    padding-left: 20px;
    position: relative;
    transition: all 0.5s;
    -webkit-transition: all 0.5s;
    -moz-transition: all 0.5s;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    justify-content: center;
}

.tree li {
    text-align: center;
    list-style-type: none;
    position: relative;
    padding: 5px 0 5px 20px;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    transition: all 0.5s;
    -webkit-transition: all 0.5s;
    -moz-transition: all 0.5s;
}

/* We will use ::before and ::after to draw the connectors */

.tree li::before, .tree li::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: 50%;
    border-left: 1px solid #ccc;
    width: 20px;
    height: 50%;
}

.tree li::after {
    bottom: auto;
    top: 50%;
    border-top: 1px solid #ccc;
}

/* We need to remove left-right connectors from elements without 
any siblings */

.tree li:only-child::after, .tree li:only-child::before {
    display: none;
}

/* Remove space from the top of single children */

.tree li:only-child {
    padding-left: 0;
}

/* Remove left connector from first child and 
right connector from last child */

.tree li:first-child::before, .tree li:last-child::after {
    border: 0 none;
}

/* Adding back the vertical connector to the last nodes */

.tree li:last-child::before {
    border-bottom: 1px solid #ccc;
    border-radius: 0 0 5px 0;
    -webkit-border-radius: 0 0 5px 0;
    -moz-border-radius: 0 0 5px 0;
}

.tree li:first-child::after {
    border-radius: 0 0 0 5px;
    -webkit-border-radius: 0 0 0 5px;
    -moz-border-radius: 0 0 0 5px;
}

/* Time to add downward connectors from parents */

.tree ul ul::before {
    content: '';
    position: absolute;
    left: 0;
    top: 50%;
    border-top: 1px solid #ccc;
    width: 20px;
    height: 0;
}

.tree li a {
    border: 1px solid #ccc;
    padding: 10px 5px;
    text-decoration: none;
    color: #777;
    font-family: arial, verdana, tahoma;
    font-size: 12px;
    display: inline-block;
    -ms-flex-item-align: center;
    -ms-grid-row-align: center;
    align-self: center;
    border-radius: 5px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    transition: all 0.5s;
    -webkit-transition: all 0.5s;
    -moz-transition: all 0.5s;
}

/* Time for some hover effects */

/* We will apply the hover effect the the lineage of the element also */

.tree li a:hover, .tree li a:hover+ul li a {
    background: #c8e4f8;
    color: #000;
    border: 1px solid #94a0b4;
}

/* Connector styles on hover */

.tree li a:hover+ul li::after, .tree li a:hover+ul li::before, .tree li a:hover+ul::before, .tree li a:hover+ul ul::before {
    border-color: #94a0b4;
}

/* Image hover effects */

img {
    /* transition: all 0.75s; */
    max-height: 80vh;
    max-width: 80vw;
    display: none;
    /* width: 0px; */
}

a.parent:hover img {
    /* width: 100%; */
    display: inline-block;
}
""".strip()
