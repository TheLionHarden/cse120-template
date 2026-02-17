from nicegui import ui

# Title
ui.label("Average Calculator").classes("text-4xl font-bold")
ui.label("Enter numbers separated by commas or spaces").classes("text-lg text-gray-500")

# Input box
input_box = ui.input(label="Numbers").props('placeholder="e.g. 1, 2, 3, 4"')

# Output box
output_label = ui.label("Average: ").classes("text-xl font-medium")

# Button to calculate average
def calculate():
    raw = input_box.value
    if not raw:
        output_label.text = "Average: "
        return
    # Split by commas first, then by spaces
    tokens = []
    for token in raw.replace(",", " ").split():
        try:
            tokens.append(float(token))
        except ValueError:
            continue  # skip non-numeric
    if tokens:
        avg = sum(tokens) / len(tokens)
        output_label.text = f"Average: {avg}"
    else:
        output_label.text = "Average: invalid input"

ui.button("Compute Average", on_click=calculate)

ui.run(title="Average Calculator", host="0.0.0.0", port=8080)
