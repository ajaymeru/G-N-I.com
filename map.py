import csv
from pyvis.network import Network

file = "data.csv"

def get_data():
    letter_data = []
    with open(file, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            letter_data.append({
                "node_a": row["node_a"],
                "node_b": row["node_b"]
            })
    return letter_data

def map_algs(g, alg="barnes"):
    if alg == "barnes":
        g.barnes_hut()
    if alg == "forced":
        g.force_atlas_2based()
    if alg == "hr":
        g.hrepulsion()

def map_data(letter_data, node_a_color="#03DAC6", node_b_color="#da03b3",
             edge_color="#018786",  node_a_shape="circle", node_b_shape="circle", alg="barnes"):
    g = Network(height="750px", width="80%", bgcolor="white", font_color="black",)
    for letter in letter_data:
        node_a = letter["node_a"]
        node_b = letter["node_b"]
        g.add_node(node_a, color=node_a_color,)
        g.add_node(node_b, color=node_b_color,)
        g.add_edge(node_a, node_b, color=edge_color)
    map_algs(g, alg=alg)
    g.show("letters.html")

letter_data = get_data()
map_data(letter_data=letter_data, node_b_shape="circle", node_a_shape="circle", alg="forced")

# Add HTML header to the output file
html_header = """
<!DOCTYPE html>
<html>
<head>
	<title>My Web Page</title>
</head>
<body>
	<img src="logo.jpg" alt="Logo" style="float:left; height:100px;">
	<img src="uni.jpg" alt="University" style="display:block; margin:auto; height:100px;">
	
	<nav style="text-align:center;">
		<ul style="display:inline-block;">
			<li style="display:inline-block; margin-right: 300px;"><a href="home.html" style="font-size:30px; font-weight:bold; text-decoration:none; color:black;">Home</a></li>
			<li style="display:inline-block; margin-right: 300px;"><a href="analysis.html" style="font-size:30px; font-weight:bold; text-decoration:none; color:black;">Analysis</a></li>
			<li style="display:inline-block;"><a href="contact.html" style="font-size:30px; font-weight:bold; text-decoration:none; color:black;">Contact Us</a></li>
		</ul>
	</nav>
"""
with open("letters.html", "r") as f:
    html_content = f.read()

with open("output.html", "w") as f:
    f.write(html_header + html_content)
