import cybox
import cybox.bindings.cybox_core_1_0 as core_binding


class DefinedObject(cybox.Entity):
    """The Cybox DefinedObject base class."""
    
    def to_obj(self):
        #TODO: subclasses should save xsi-type
        raise NotImplementedError()

    def to_dict(self):
        #TODO: subclasses should save xsi-type
        raise NotImplementedError()

    @staticmethod
    def from_obj(defobj_obj):
        if not defobj_obj:
            return None
        any_attributes = defobj_obj.get_anyAttributes_()
        xsi_type = any_attributes.get('{http://www.w3.org/2001/XMLSchema-instance}type')
        if not xsi_type:
            raise ValueError("Object has no xsi-type")
        type_value = xsi_type.split(':')[1]

        # Find the class that can parse this type.
        klass = cybox.utils.get_class_for_object_type(type_value)

        return klass.from_obj(defobj_obj)


    @staticmethod
    def from_dict(defobj_dict):
        if not defobj_dict:
            return None
        
        xsi_type = defobj_dict.get('xsi_type', None)
        if not xsi_type:
            raise ValueError('dictionary does not have xsi_type key')
        
        klass = cybox.utils.get_class_for_object_type(xsi_type)
        defobj = klass.from_dict(defobj_dict)
        
        return defobj