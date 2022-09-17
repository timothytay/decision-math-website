from flask import Flask, request, render_template, flash, session
from processes import sort_items, find_mst, bin_pack
import re

app = Flask(__name__, template_folder="template")
app.config["SECRET_KEY"] = "ashdgfyuiwerghfjk;abhsdfjkasghdfksgdlfjksgdfhjklgblskadf"


@app.route("/")
def index():
	return render_template("homepage.html")

@app.route("/bin-packing", methods=["GET", "POST"])

def bin():
	if "numbers" not in session:
		session["numbers"] = []
	if "bin" not in session:
		session["bin"] = None
	error = ""
	output = ""
	values = ""
	data = ""
	output_type = "Values"
	if request.method == "POST":

		if request.form["action"] == "Add Value" and request.form.get("value"):

			try:
				session["numbers"].append(float(request.form["value"]))
				session.modified = True
			except:
				error = "Please enter a numeric value."

		if request.form["action"] == "Set Size" and request.form.get("bin"):
			try:
				session["bin"] = float(request.form["bin"])
				session.modified = True
				print(session["bin"])
			except:
				error = "Please enter a numeric value."

		if request.form["action"] == "Pack":
			if len(session["numbers"]) > 1 and session["bin"]:

				output = bin_pack(session["numbers"], float(session["bin"])).split("\n")
				session["numbers"] = []
				session["bin"] = None
				session.modified = True
				output_type = "Output"
				
			else:
				error = "Please set a bin size and submit at least two values to pack."

		if request.form["action"] == "Reset":
			session["numbers"] = []
			session.modified = True
			error = ""
			output = ""
			output_type = "Values"

		if len(session["numbers"]) > 0:
			data += "Numbers: "+", ".join([str(number) for number in session["numbers"]])
			output = data.split("\n")

		if session["bin"]:
			data += f"\nBin Size: {session['bin']}"
			output = data.split("\n")

	return render_template("bin.html", output_type = output_type, error=error, output=output)





@app.route("/bubble-sort", methods=["GET", "POST"])
def bubble():
	if "value_list" not in session:
		session["value_list"] = []
	error = ""
	output = ""
	values = ""
	output_type = "Values"
	if request.method == "POST":

		if request.form.get("value"):

			try:
				session["value_list"].append(float(request.form["value"]))
				session.modified = True
			except:
				error = "Please enter a numeric value"

		if request.form["action"] == "Sort":
			if len(session["value_list"]) > 1:

				output = sort_items(session["value_list"]).split("\n")
				session["value_list"] = []
				session.modified = True
				output_type = "Output"
				values = ""

			else:
				error = "Please submit at least two values to sort."

		if request.form["action"] == "Reset":
			session["value_list"] = []
			session.modified = True
			error = ""
			output = ""
			output_type = "Values"

		if len(session["value_list"]) > 0:
			values = ", ".join([str(number) for number in session["value_list"]])

	return render_template("bubble.html", output_type = output_type, error=error, output=output, numbers=values)




@app.route("/mst-finder", methods=["GET", "POST"])

def mst():
	if "edges" not in session:
		session["edges"] = {}
	if "vertices" not in session:
		session["vertices"] = []
	output = ""
	error = ""
	output_type = "Edges"

	if request.method == "POST":

		if request.form["action"] == "Reset":
			output_type = "Edges"
			session["edges"] = {}
			session["vertices"] = []
			session.modified = True

		if request.form["action"] == "Find":
			print(session["edges"])
			print(session["vertices"])
			if len(session["edges"]) > 1:
				output = find_mst(session["edges"], session["vertices"])
				session["edges"] = {}
				session["vertices"] = []
				session.modified = True
				output_type = "Answer"
			else:
				error = "Please add at least two edges to find the minimum spanning tree."

		if request.form["action"] == "Add Edge":
			if request.form.get("edge") and request.form.get("edge_weight"):

				if (
					re.search("^[a-z]{2}$", request.form["edge"], re.IGNORECASE)
					and request.form["edge"][0] != request.form["edge"][1]
					and request.form["edge"].upper() not in list(session["edges"].keys())
					and request.form["edge"][::-1].upper() not in list(session["edges"].keys())
				):
					try:
						session["edges"][request.form["edge"].upper()] = float(
							request.form["edge_weight"]
						)
						for vertice in list(request.form["edge"]):
							if vertice.upper() not in session["vertices"]:
								session["vertices"].append(vertice.upper())
						session.modified = True
					except:
						error = "Please enter a numeric value for the edge weight."
				else:
					error = (
						"Please enter a unique edge in the correct format (e.g. CD)."
					)
			else:
				error = "Please enter both the edge and the edge weight to add an edge."

	if "edges" in session and len(session["edges"]) > 0:
		output = ""
		for edge, weight in session["edges"].items():
			output += f"{edge}({weight}), "

	return render_template("mst.html", error=error, output_type=output_type, output=output)


if __name__ == "__main__":
	app.run(debug=True)
