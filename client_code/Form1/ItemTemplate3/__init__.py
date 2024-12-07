from ._anvil_designer import ItemTemplate3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate3(ItemTemplate3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def edit_nosql_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('update_nosql', 
                      self.tb_nombre_nosql.text,
                      self.tb_apellido_nosql.text,
                      self.tb_materia_nosql.text,
                      self.tb_nota_nosql.text,
                      int(self.id_nosql_label.text))

  def delete_nosql_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('delete_from_nosql', 
                      self.tb_nombre_nosql.text,
                      self.tb_apellido_nosql.text,
                      self.tb_materia_nosql.text,
                      self.tb_nota_nosql.text)
    self.item.delete()
    self.remove_from_parent()



