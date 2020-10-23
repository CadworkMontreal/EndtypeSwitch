# Copyright 2020 Cadwork.
# All rights reserved.
# This file is part of EndtypeSwitch,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

# import required controllers
import utility_controller, element_controller, endtype_controller, attribute_controller, visualization_controller


#get active elements
active_elements = element_controller.get_active_identifiable_element_ids()

#create ellowed elements list
active_allowed = []
for element in active_elements:
    if attribute_controller.is_beam(element):
        active_allowed.append(element)
    if attribute_controller.is_panel(element):
    		active_allowed.append(element)

#querry endtype to replace
old_endtype = utility_controller.get_user_string("name of the end-type to replace")

# endtypes available?
if endtype_controller.get_endtype_id(old_endtype) == 0:
    utility_controller.print_error("No such end-type")
    exit()

#new end type
new_endtype = utility_controller.get_user_string("name of the new end-type")

# endtypes available?
if endtype_controller.get_endtype_id(new_endtype) == 0:
    utility_controller.print_error("No such end-type")
    exit()

#number of changed endtype
replaced_end_types = 0

#list of changed elements
changed_element = []

#Loop over element with old endtype
for element in active_allowed:
    if endtype_controller.get_endtype_name_start(element) == old_endtype:
        endtype_controller.set_endtype_name_start(element, new_endtype)
        replaced_end_types = replaced_end_types + 1
        changed_element.append(element)
    if endtype_controller.get_endtype_name_end(element) == old_endtype:
        endtype_controller.set_endtype_name_end(element, new_endtype)
        replaced_end_types = replaced_end_types + 1
        changed_element.append(element)

#activate changed elements
visualization_controller.set_inactive(active_elements)
visualization_controller.set_active(changed_element)
utility_controller.print_error("Number of end-type replaced:%d" % replaced_end_types)
