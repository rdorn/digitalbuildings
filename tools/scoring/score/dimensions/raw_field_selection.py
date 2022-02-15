# Copyright 2022 Google LLC
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
""" Core component """

from score.dimensions.dimension import Dimension
from score.types_ import TranslationsDict
from score.constants import FileTypes

PROPOSED, SOLUTION = FileTypes


class RawFieldSelection(Dimension):
  """
  Quantifies whether the correct raw fields
  (e.g. "points.chilled_water_flowrate_sensor.present_value")
  were mapped (versus ignored) in the proposed file.
  """
  def __init__(self, *, translations: TranslationsDict):
    super().__init__(translations=translations)

    # Combine translations for all devices within the dictionary
    solution_condensed = [
        matched_translations[SOLUTION]
        for matched_translations in translations.values()
        if matched_translations[SOLUTION]
    ]
    # Account for empty list
    solution_translations = solution_condensed and solution_condensed[0]

    proposed_condensed = [
        matched_translations[PROPOSED]
        for matched_translations in translations.values()
        if matched_translations[PROPOSED]
    ]
    # Account for empty list
    proposed_translations = proposed_condensed and proposed_condensed[0]

    solution_fields = set([
        translation.raw_field_name
        for standard_field_name, translation in solution_translations
    ])

    proposed_fields = set([
        translation.raw_field_name
        for standard_field_name, translation in proposed_translations
    ])

    correct_fields = proposed_fields.intersection(solution_fields)
    incorrect_fields = proposed_fields.difference(solution_fields)

    self.correct_reporting = len(correct_fields)
    self.correct_ceiling_reporting = len(set(solution_translations))
    self.incorrect_reporting = len(incorrect_fields)
