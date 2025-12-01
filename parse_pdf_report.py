import sys, json;
report = json.load(sys.stdin)
output = {
  "metadata": {
    "title": report[0]["blocks"][7]["lines"][0]["spans"][0]["text"],
    "language": report[0]["blocks"][7]["lines"][4]["spans"][0]["text"],
  },

  "checks": {
      "pdf_syntax": {
          "success": report[0]["blocks"][2]["lines"][0]["spans"][2]["text"],
          "warning": report[0]["blocks"][2]["lines"][0]["spans"][4]["text"],
          "failure": report[0]["blocks"][2]["lines"][0]["spans"][6]["text"],
      },
      "fonts": {
          "success": report[0]["blocks"][2]["lines"][1]["spans"][2]["text"],
          "warning": report[0]["blocks"][2]["lines"][1]["spans"][4]["text"],
          "failure": report[0]["blocks"][2]["lines"][1]["spans"][6]["text"],
      },
      "content": {
          "success": report[0]["blocks"][2]["lines"][2]["spans"][2]["text"],
          "warning": report[0]["blocks"][2]["lines"][2]["spans"][4]["text"],
          "failure": report[0]["blocks"][2]["lines"][2]["spans"][6]["text"],
      },
      "embedded_files": {
          "success": report[0]["blocks"][2]["lines"][3]["spans"][2]["text"],
          "warning": report[0]["blocks"][2]["lines"][3]["spans"][4]["text"],
          "failure": report[0]["blocks"][2]["lines"][3]["spans"][6]["text"],
      },
      "natural_language": {
          "success": report[0]["blocks"][2]["lines"][4]["spans"][2]["text"],
          "warning": report[0]["blocks"][2]["lines"][4]["spans"][4]["text"],
          "failure": report[0]["blocks"][2]["lines"][4]["spans"][6]["text"],
      },

     "structural_elements": {
          "success": report[0]["blocks"][3]["lines"][0]["spans"][2]["text"],
          "warning": report[0]["blocks"][3]["lines"][0]["spans"][4]["text"],
          "failure": report[0]["blocks"][3]["lines"][0]["spans"][6]["text"],
      },
      "structure_tree": {
          "success": report[0]["blocks"][3]["lines"][1]["spans"][2]["text"],
          "warning": report[0]["blocks"][3]["lines"][1]["spans"][4]["text"],
          "failure": report[0]["blocks"][3]["lines"][1]["spans"][6]["text"],
      },
      "role_mapping": {
          "success": report[0]["blocks"][3]["lines"][2]["spans"][2]["text"],
          "warning": report[0]["blocks"][3]["lines"][2]["spans"][4]["text"],
          "failure": report[0]["blocks"][3]["lines"][2]["spans"][6]["text"],
      },
      "alternative_descriptions": {
          "success": report[0]["blocks"][3]["lines"][3]["spans"][2]["text"],
          "warning": report[0]["blocks"][3]["lines"][3]["spans"][4]["text"],
          "failure": report[0]["blocks"][3]["lines"][3]["spans"][6]["text"],
      },

      "metadata": {
          "success": report[0]["blocks"][4]["lines"][0]["spans"][2]["text"],
          "warning": report[0]["blocks"][4]["lines"][0]["spans"][4]["text"],
          "failure": report[0]["blocks"][4]["lines"][0]["spans"][6]["text"],
      },
      "document_settings": {
          "success": report[0]["blocks"][4]["lines"][1]["spans"][2]["text"],
          "warning": report[0]["blocks"][4]["lines"][1]["spans"][4]["text"],
          "failure": report[0]["blocks"][4]["lines"][1]["spans"][6]["text"],
      },
  }
}
for check, statuses in output["checks"].items():
    total = 0
    for status, value in statuses.items():
        value = 0 if value == "-" else int(value)
        statuses[status] = value
        total += value
    statuses["total"] = total
print(json.dumps(output))

