from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.repeating_panel_1.items = app_tables.table_bdd_relacional.search()
    self.repeating_panel_2.items = app_tables.table_bdd_nosql.search()

  def button_agregar_datos_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Lo mando a la bdd relacional del notebook
    result = anvil.server.call('add_to_database', 
                              self.input_nombre.text,
                              self.input_apellido.text,
                              self.input_materia.text,
                              self.input_nota.text)
    if result:
      #self.result_1.visible = True
      #self.result_1.text = str(result).capitalize()
      #Agrego al panel de la interfaz
      app_tables.table_bdd_relacional.add_row(codigo_materia_tb = self.input_materia.text,
                                              apellido_tb=self.input_apellido.text,
                                              nota_tb=self.input_nota.text,
                                             nombre_tb=self.input_nombre.text,
                                             id_tb=str(result))
      #Actualizo el panel de la interfaz con la nueva data
      self.repeating_panel_1.items = app_tables.table_bdd_relacional.search()
      #Limpio las celdas de input
      self.input_nombre.text = ''
      self.input_apellido.text = ''
      self.input_materia.text = ''
      self.input_nota.text = ''

  def button_agregar_datos2_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = anvil.server.call('add_to_nosql', 
                              self.input_nombre.text,
                              self.input_apellido.text,
                              self.input_materia.text,
                              self.input_nota.text)
    if result:
      #self.result_1.visible = True
      #self.result_1.text = str(result).capitalize()
      #Agrego al panel de la interfaz
      app_tables.table_bdd_nosql.add_row(materia_tb_nosql = self.input_materia.text,
                                              apellido_tb_nosql=self.input_apellido.text,
                                              nota_tb_nosql=self.input_nota.text,
                                             nombre_tb_nosql=self.input_nombre.text,
                                             id_tb_nosql=result)
      #Actualizo el panel de la interfaz con la nueva data
      self.repeating_panel_2.items = app_tables.table_bdd_nosql.search()
      #Limpio las celdas de input
      self.input_nombre.text = ''
      self.input_apellido.text = ''
      self.input_materia.text = ''
      self.input_nota.text = ''

      
      
      
      
      
