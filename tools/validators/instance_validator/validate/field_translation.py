# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Translation of a single field."""

class FieldTranslation(object):
  """A translation for a single field of an entity.

  Args:
    field_name: name of the field the translation corresponds to
    units: dictionary from standard units to expected telemetry units
    states: dictionary from standard states to expected telemetry states
  """

  def __init__(self, field_name, units, states):
    super().__init__()
    self.field_name = field_name
    self.units = units
    self.states = states