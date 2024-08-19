from app.models.modelsbase import Model, Column, String, Integer, Boolean, ForeignKey


# Define the model
class CustomfieldOptions(Model):

    __tablename__ = 'customfield_options'

    field_id = Column(String)
    id = Column(String, nullable=False)
    value = Column(String(80), nullable=False)
    parentId = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Item {self.value}>"

    def toggle(self):
        if self.enabled == True:
            self.update(enabled=False)
        else:
            self.update(enabled=True)

    def to_dict(self):
        return {"id": self.id, "value": self.value, "parentId": self.parentId, "enabled": self.enabled}