

## CLASSES

class Definition(object):
    """
    base class
    """
    def __init__(self,
                 name=None,
                 singular_name=None,
                 is_a=None,
                 description=None,
                 abstract=None,
                 mappings=None):
        self.name=name
        self.singular_name=singular_name
        self.is_a=is_a
        self.description=description
        self.abstract=abstract
        self.mappings=mappings

    def __str__(self):
        return "name={} singular_name={} is_a={} description={} abstract={} mappings={} ".format(self.name,self.singular_name,self.is_a,self.description,self.abstract,self.mappings)
    def __repr__(self):
        return self.__str__()


class SlotDefinition(Definition):
    """
    A property or slot
    """
    def __init__(self,
                 mixin=None,
                 mixins=None,
                 identifier=None,
                 domain=None,
                 range=None,
                 multivalued=None,
                 required=None,
                 path=None,
                 subproperty_of=None,
                 name=None,
                 singular_name=None,
                 is_a=None,
                 description=None,
                 abstract=None,
                 mappings=None):
        self.mixin=mixin
        self.mixins=mixins
        self.identifier=identifier
        self.domain=domain
        self.range=range
        self.multivalued=multivalued
        self.required=required
        self.path=path
        self.subproperty_of=subproperty_of
        self.name=name
        self.singular_name=singular_name
        self.is_a=is_a
        self.description=description
        self.abstract=abstract
        self.mappings=mappings

    def __str__(self):
        return "mixin={} mixins={} identifier={} domain={} range={} multivalued={} required={} path={} subproperty_of={} name={} singular_name={} is_a={} description={} abstract={} mappings={} ".format(self.mixin,self.mixins,self.identifier,self.domain,self.range,self.multivalued,self.required,self.path,self.subproperty_of,self.name,self.singular_name,self.is_a,self.description,self.abstract,self.mappings)
    def __repr__(self):
        return self.__str__()


class SlotUsageDefinition(SlotDefinition):
    """
    A usage of slot in the context of a class
    """
    def __init__(self,
                 mixin=None,
                 mixins=None,
                 identifier=None,
                 domain=None,
                 range=None,
                 multivalued=None,
                 required=None,
                 path=None,
                 subproperty_of=None,
                 name=None,
                 singular_name=None,
                 is_a=None,
                 description=None,
                 abstract=None,
                 mappings=None):
        self.mixin=mixin
        self.mixins=mixins
        self.identifier=identifier
        self.domain=domain
        self.range=range
        self.multivalued=multivalued
        self.required=required
        self.path=path
        self.subproperty_of=subproperty_of
        self.name=name
        self.singular_name=singular_name
        self.is_a=is_a
        self.description=description
        self.abstract=abstract
        self.mappings=mappings

    def __str__(self):
        return "mixin={} mixins={} identifier={} domain={} range={} multivalued={} required={} path={} subproperty_of={} name={} singular_name={} is_a={} description={} abstract={} mappings={} ".format(self.mixin,self.mixins,self.identifier,self.domain,self.range,self.multivalued,self.required,self.path,self.subproperty_of,self.name,self.singular_name,self.is_a,self.description,self.abstract,self.mappings)
    def __repr__(self):
        return self.__str__()


class ClassDefinition(Definition):
    """
    A class or interface
    """
    def __init__(self,
                 defining_slots=None,
                 subclass_of=None,
                 mixin=None,
                 mixins=None,
                 slots=None,
                 slot_usage=None,
                 name=None,
                 singular_name=None,
                 is_a=None,
                 description=None,
                 abstract=None,
                 mappings=None):
        self.defining_slots=defining_slots
        self.subclass_of=subclass_of
        self.mixin=mixin
        self.mixins=mixins
        self.slots=slots
        self.slot_usage=slot_usage
        self.name=name
        self.singular_name=singular_name
        self.is_a=is_a
        self.description=description
        self.abstract=abstract
        self.mappings=mappings

    def __str__(self):
        return "defining_slots={} subclass_of={} mixin={} mixins={} slots={} slot_usage={} name={} singular_name={} is_a={} description={} abstract={} mappings={} ".format(self.defining_slots,self.subclass_of,self.mixin,self.mixins,self.slots,self.slot_usage,self.name,self.singular_name,self.is_a,self.description,self.abstract,self.mappings)
    def __repr__(self):
        return self.__str__()


class TypeDefinition(Definition):
    """
    A type definition
    """
    def __init__(self,
                 mixins=None,
                 name=None,
                 singular_name=None,
                 is_a=None,
                 description=None,
                 abstract=None,
                 mappings=None):
        self.mixins=mixins
        self.name=name
        self.singular_name=singular_name
        self.is_a=is_a
        self.description=description
        self.abstract=abstract
        self.mappings=mappings

    def __str__(self):
        return "mixins={} name={} singular_name={} is_a={} description={} abstract={} mappings={} ".format(self.mixins,self.name,self.singular_name,self.is_a,self.description,self.abstract,self.mappings)
    def __repr__(self):
        return self.__str__()


class SchemaDefinition(Definition):
    """
    A collection of definitions
    """
    def __init__(self,
                 id=None,
                 slots=None,
                 classes=None,
                 types=None,
                 name=None,
                 singular_name=None,
                 is_a=None,
                 description=None,
                 abstract=None,
                 mappings=None):
        self.id=id
        self.slots=slots
        self.classes=classes
        self.types=types
        self.name=name
        self.singular_name=singular_name
        self.is_a=is_a
        self.description=description
        self.abstract=abstract
        self.mappings=mappings

    def __str__(self):
        return "id={} slots={} classes={} types={} name={} singular_name={} is_a={} description={} abstract={} mappings={} ".format(self.id,self.slots,self.classes,self.types,self.name,self.singular_name,self.is_a,self.description,self.abstract,self.mappings)
    def __repr__(self):
        return self.__str__()


