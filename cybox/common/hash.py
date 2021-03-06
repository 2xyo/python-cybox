import cybox
import cybox.bindings.cybox_common_types_1_0 as common_binding
from cybox.common.attributes import HashName, SimpleHashValue

class Hash(cybox.Entity):
    TYPE_MD5 = "MD5"
    TYPE_MD6 = "MD6"
    TYPE_SHA1 = "SHA1"
    TYPE_SHA256 = "SHA256"
    TYPE_SSDEEP = "SSDEEP"
    TYPE_OTHER = "Other"
    AUTO_TYPE = "auto"

    def __init__(self, hash_value=None, type_=AUTO_TYPE, exact=False):
        """Create a new Hash Object

        Attempts to guess the type of hash based on its length.
        If exact=True, add 'condition="Equals"' to the hash_value
        """
        self.simple_hash_value = hash_value

        if type_ == self.AUTO_TYPE:
            if not hash_value:
                # If not provided or an empty string, don't assign the type
                self.type_ = None
            elif len(hash_value) == 32:
                self.type_ = Hash.TYPE_MD5
            elif len(hash_value) == 40:
                self.type_ = Hash.TYPE_SHA1
            elif len(hash_value) == 64:
                self.type_ = Hash.TYPE_SHA256
            else:
                self.type_ = Hash.TYPE_OTHER
        else:
            self.type_ = type_

        if exact:
            self.simple_hash_value.condition = "Equals"

    # Properties
    @property
    def type_(self):
        return self._type

    @type_.setter
    def type_(self, value):
        if value and not isinstance(value, HashName):
            value = HashName(value)
        self._type = value

    @property
    def simple_hash_value(self):
        return self._simple_hash_value

    @simple_hash_value.setter
    def simple_hash_value(self, value):
        if value and not isinstance(value, SimpleHashValue):
            value = SimpleHashValue(value)
        self._simple_hash_value = value

    # Other_Type and FuzzyHashes not yet supported.

    # Import/Export
    def to_obj(self):
        hashobj = common_binding.HashType()
        hashobj.set_Type(self.type_.to_obj())
        hashobj.set_Simple_Hash_Value(self.simple_hash_value.to_obj())

        return hashobj

    def to_dict(self):
        return {
            'type': self.type_.to_dict(),
            'simple_hash_value': self.simple_hash_value.to_dict()
        }

    @staticmethod
    def from_obj(hash_obj):
        if not hash_obj:
            return None
        hash_ = Hash()
        hash_.type_ = HashName.from_obj(hash_obj.get_Type())
        hash_.simple_hash_value = SimpleHashValue.from_obj(hash_obj.get_Simple_Hash_Value())
        return hash_

    @staticmethod
    def from_dict(hash_dict):
        if not hash_dict:
            return None
        hash_ = Hash()
        hash_.type_ = HashName.from_dict(hash_dict.get('type'))
        hash_.simple_hash_value = SimpleHashValue.from_dict(
                                        hash_dict.get('simple_hash_value'))
        return hash_

#    @classmethod
#    def object_from_dict(cls, hash_dict):
#        """Create the Hash object representation from an input dictionary"""
#        hash = common_binding.HashType()
#        for hash_key, hash_value in hash_dict.items():
#            if hash_key == 'type' : hash.set_Type(Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),hash_value))
#            if hash_key == 'other_type' : hash.set_Type(Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),hash_value))
#            if hash_key == 'simple_hash_value' : hash.set_Simple_Hash_Value(Base_Object_Attribute.object_from_dict(common_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),hash_value))
#            if hash_key == 'fuzzy_hash_value' : hash.set_Fuzzy_Hash_Value(Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),hash_value))
#            if hash_key == 'fuzzy_hash_structure':
#                for fuzzy_hash_structure_dict in hash_value:
#                    fuzzy_hash_structure_object = common_binding.FuzzyHashStructureType()
#                    for fuzzy_key, fuzzy_value in fuzzy_hash_structure_dict.items():
#                        if fuzzy_key == 'block_size' : fuzzy_hash_structure_object.set_Block_Size(Base_Object_Attribute.object_from_dict(common_binding.IntegerObjectAttributeType(datatype='Integer'),fuzzy_value))
#                        if fuzzy_key == 'block_hash' : 
#                            block_hash_dict = fuzzy_value
#                            block_hash_object = common_binding.FuzzyHashBlockType()
#                            for block_hash_key, block_hash_value in block_hash_dict.items():
#                                if block_hash_key == 'segment_count' : block_hash_object.set_Segment_Count(Base_Object_Attribute.object_from_dict(common_binding.IntegerObjectAttributeType(datatype='Integer'),block_hash_value))
#                                if block_hash_key == 'block_hash_value' :
#                                    hash_value_dict = block_hash_value
#                                    hash_value_object = common_binding.HashValueType()
#                                    for hash_value_key, hash_value_value in hash_value_dict.items():
#                                        if hash_value_key == 'simple_hash_value' : hash_value_object.set_Simple_Hash_Value(Base_Object_Attribute.object_from_dict(common_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),hash_value_value))
#                                        if hash_value_key == 'fuzzy_hash_value' : hash_value_object.set_Fuzzy_Hash_Value(Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),hash_value_value))
#                                    if hash_value_object.hasContent_(): block_hash_object.set_Block_Hash_Value(hash_value_object)
#                                if block_hash_key == 'segments' :
#                                    segments_dict = block_hash_value
#                                    segments_object = common_binding.HashSegmentsType()
#                                    for segment in segments_dict:
#                                        hash_segment_object = common_binding.HashSegmentType()
#                                        for segment_key, segment_value in segment.items():
#                                            if segment_key == 'trigger_point' : hash_segment_object.set_Trigger_Point(Base_Object_Attribute.object_from_dict(common_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),segment_value))
#                                            if segment_key == 'segment_hash' :
#                                                segment_hash_dict = segment_value
#                                                segment_hash_object = common_binding.HashValueType()
#                                                for segment_hash_key, segment_hash_value in segment_hash_dict.items():
#                                                    if segment_hash_key == 'simple_hash_value' : segment_hash_object.set_Simple_Hash_Value(Base_Object_Attribute.object_from_dict(common_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),segment_hash_value))
#                                                    if segment_hash_key == 'fuzzy_hash_value' : segment_hash_object.set_Fuzzy_Hash_Value(Base_Object_Attribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),segment_hash_value))
#                                                if segment_hash_object.hasContent_(): hash_segment_object.set_Segment_Hash(segment_hash_object)
#                                            if segment_key == 'raw_segment_content' : hash_segment_object.set_Raw_Segment_Content(segment_value)
#                                        if hash_segment_object.hasContent_() : segments_object.add_Segment(hash_segment_object)
#                                    if segments_object.hasContent_() : block_hash_object.set_Segments(segments_object)
#                            if block_hash_object.hasContent_() : fuzzy_hash_structure_object.set_Block_Hash(block_hash_object)
#                    if fuzzy_hash_structure_object.hasContent_() : hash.add_Fuzzy_Hash_Structure(fuzzy_hash_structure_object)
#
#        return hash


class HashList(cybox.Entity):
    def __init__(self):
        self.hashes = []

    def add(self, hash_):
        self.hashes.append(hash_)

    def to_obj(self):
        hashlist_obj = common_binding.HashListType()
        for hash_ in self.hashes:
            hashlist_obj.add_Hash(hash_.to_obj())
        return hashlist_obj

    def to_dict(self):
        return [h.to_dict() for h in self.hashes]

    @staticmethod
    def from_obj(hashlist_obj):
        if not hashlist_obj:
            return None
        hashlist = HashList()
        hashlist.hashes = [Hash.from_obj(h) for h in hashlist_obj.get_Hash()]
        return hashlist

    @staticmethod
    def from_dict(hashlist_dict):
        if not hashlist_dict:
            return None
        # Hashlist_dict should really be a list, not a dict
        hashlist = HashList()
        hashlist.hashes = [Hash.from_dict(h) for h in hashlist_dict]
        return hashlist
