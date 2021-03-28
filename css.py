CSS = """
/* Credits */

/* Ilya Pestov: Original, https://codepen.io/Pestov/pen/BLpgm */
/* Paul Smirnov: Horizontal, https://codepen.io/paulsmirnov/pen/dyyOLwa */
/* Background pattern, https://projects.verou.me/css3patterns/ */
/* Shane Drabing: Changed styling, added image hover effects */

/* Variables */

:root {
    --border-radius: 3px;
    --border-width: 2px;
    --border-padding: 10px;
    --transition-speed: 0.5s;

    --bg-color1: hsl(210, 10%, 50%);
    --bg-color2: hsl(210, 10%, 52%);

    --box-color: hsl(0, 0%, 75%);
    --border-color: hsl(0, 0%, 75%);
    --text-color: hsl(0, 0%, 25%);

    --box-color-hover: hsl(0, 0%, 100%);
    --border-color-hover: hsl(0, 0%, 100%);
    --text-color-hover: hsl(0, 0%, 0%);
}

/* Now the CSS */

* {
    margin: 0;
    padding: 0;
}

body {
    background:
    radial-gradient(circle at 100% 50%, transparent 19%, var(--bg-color1) 20%, var(--bg-color1) 35.4%, transparent 36.4%, transparent),
    radial-gradient(circle at 0% 50%, transparent 19%, var(--bg-color1) 20%, var(--bg-color1) 35.4%, transparent 36.4%, transparent) 0 30px;
    background-color: var(--bg-color2);
    background-size: 40px 60px;
    
}

.tree {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-pack: start;
    -ms-flex-pack: start;
    justify-content: flex-start;
    padding-right: 100px;
    padding-bottom: 300px;
}

.tree ul {
    padding-left: var(--border-padding);
    position: relative;
    transition: all var(--transition-speed);
    -webkit-transition: all var(--transition-speed);
    -moz-transition: all var(--transition-speed);
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
    padding: var(--border-radius) 0 var(--border-radius) var(--border-padding);
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    transition: all var(--transition-speed);
    -webkit-transition: all var(--transition-speed);
    -moz-transition: all var(--transition-speed);
}

/* We will use ::before and ::after to draw the connectors */

.tree li::before, .tree li::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: 50%;
    border-left: var(--border-width) solid var(--border-color);
    width: var(--border-padding);
    height: 50%;
}

.tree li::after {
    bottom: auto;
    top: 50%;
    border-top: var(--border-width) solid var(--border-color);
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
    border-bottom: var(--border-width) solid var(--border-color);
    border-radius: 0 0 var(--border-radius) 0;
    -webkit-border-radius: 0 0 var(--border-radius) 0;
    -moz-border-radius: 0 0 var(--border-radius) 0;
}

.tree li:first-child::after {
    border-radius: 0 0 0 var(--border-radius);
    -webkit-border-radius: 0 0 0 var(--border-radius);
    -moz-border-radius: 0 0 0 var(--border-radius);
}

/* Time to add downward connectors from parents */

.tree ul ul::before {
    content: '';
    position: absolute;
    left: 0;
    top: 50%;
    border-top: var(--border-width) solid var(--border-color);
    width: var(--border-padding);
    height: 0;
}

/* Box styles */

.tree li a {
    border: var(--border-width) solid var(--border-color);
    padding: 4px 8px;
    text-decoration: none;
    color: var(--text-color);
    background-color: var(--box-color);
    font-family: arial, verdana, tahoma;
    font-size: 12px;
    display: flex-end;
    -ms-flex-item-align: center;
    -ms-grid-row-align: center;
    align-self: center;
    border-radius: var(--border-radius);
    -webkit-border-radius: var(--border-radius);
    -moz-border-radius: var(--border-radius);
    transition: all var(--transition-speed);
    -webkit-transition: all var(--transition-speed);
    -moz-transition: all var(--transition-speed);
}

/* Time for some hover effects */

/* We will apply the hover effect the the lineage of the element also */

.tree li a:hover, .tree li a:hover+ul li a {
    background: var(--box-color-hover);
    color: var(--text-color-hover);
    border: var(--border-width) solid var(--border-color-hover);
}

/* Connector styles on hover */

.tree li a:hover+ul li::after, .tree li a:hover+ul li::before, .tree li a:hover+ul::before, .tree li a:hover+ul ul::before {
    border-color: var(--border-color-hover);
}

/* Image hover effects */

img {
    transition: all var(--transition-speed);
    -webkit-transition: all var(--transition-speed);
    -moz-transition: all var(--transition-speed);
    transition-timing-function: ease-out;

    width: auto;
    height: auto;
    max-width: 0px;
    max-height: 0px;
}

a.parent:hover img {
    width: auto;
    height: auto;
    max-width: 75vw;
    max-height: 50vh;
}
""".strip()
