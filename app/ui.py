# app/ui.py
from nicegui import ui

# Root page
ui.label('Graduate Program Dashboard').classes('text-4xl font-bold')
ui.label('Real-time student appointment tracking').classes('text-lg text-gray-500')

ui.run(title='Average Workshop UI', host='0.0.0.0', port=8080)
