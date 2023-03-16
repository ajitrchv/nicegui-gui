from nicegui import ui

def addNow():
    ui.notify("Added Task!")
    with tasks:
        with ui.row() as row:
            ui.label(name.value)
            ui.button("Update", on_click=lambda: details(row))
            ui.button(on_click=lambda:remove(row)).props("flat icon=delete color=red")
    
def details(row):
    print(row.id)
    print(row)
    row.style("color:red")
    print(row.default_slot.children[0].text)
    
    row.default_slot.children[0].text = name.value
    
    row.update()

def remove(row):
    tasks.remove(row)
    tasks.update()

    
            
name = ui.input(label="Name")
ui.button("add", on_click=addNow)
tasks = ui.column()
ui.run()
    