from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refresh_data_bindings is called"""
    pass

  def delete_button_relacional_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('delete_from_database', 
                      self.tb_nombre_rp.text,
                      self.tb_apellido_rp.text,
                      self.tb_materia_rp.text,
                      self.tb_nota_rp.text)
    self.item.delete()
    self.remove_from_parent()

  def edit_button_sql_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('update_database', 
                      self.tb_nombre_rp.text,
                      self.tb_apellido_rp.text,
                      self.tb_materia_rp.text,
                      self.tb_nota_rp.text,
                      int(self.id_tb_rp.text))
    
