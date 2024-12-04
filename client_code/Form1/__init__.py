from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_agregar_datos_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = anvil.server.call('add_to_database', 
                               self.input_nombre.text,
                              self.input_apellido.text,
                              self.input_materia.text,
                              self.input_nota.text)
    if result:
      self.result_1.visible = True
      self.result_1.text = result.capitalize()
      
      
