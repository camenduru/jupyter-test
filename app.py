from notebook.notebookapp import NotebookApp
app = NotebookApp()
app.initialize(["--port", str(7860), "--ip", "0.0.0.0", "--NotebookApp.token", "", "--no-browser", "--NotebookApp.tornado_settings", "{'headers': {'Content-Security-Policy': 'frame-ancestors *'}}"])
app.start()