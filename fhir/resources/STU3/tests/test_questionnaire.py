#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 on 2019-01-17.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import questionnaire
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class QuestionnaireTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Questionnaire", js["resourceType"])
        return questionnaire.Questionnaire(js)
    
    def testQuestionnaire1(self):
        inst = self.instantiate_from("questionnaire-example-gcs.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire1(inst)
        
        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire1(inst2)
    
    def implQuestionnaire1(self, inst):
        self.assertEqual(force_bytes(inst.code[0].code), force_bytes("9269-2"))
        self.assertEqual(force_bytes(inst.code[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("motor"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("verbal"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("eye"))
        self.assertEqual(inst.date.date, FHIRDate("2015-08-03").date)
        self.assertEqual(inst.date.as_json(), "2015-08-03")
        self.assertEqual(force_bytes(inst.id), force_bytes("gcs"))
        self.assertEqual(force_bytes(inst.item[0].code[0].code), force_bytes("9270-0"))
        self.assertEqual(force_bytes(inst.item[0].code[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.item[0].linkId), force_bytes("1.1"))
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("choice"))
        self.assertEqual(force_bytes(inst.item[1].code[0].code), force_bytes("9268-4"))
        self.assertEqual(force_bytes(inst.item[1].code[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.item[1].linkId), force_bytes("1.2"))
        self.assertEqual(force_bytes(inst.item[1].type), force_bytes("choice"))
        self.assertEqual(force_bytes(inst.item[2].code[0].code), force_bytes("9267-6"))
        self.assertEqual(force_bytes(inst.item[2].code[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.item[2].linkId), force_bytes("1.3"))
        self.assertEqual(force_bytes(inst.item[2].type), force_bytes("choice"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project team"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.subjectType[0]), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Glasgow Coma Score"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/Questionnaire/gcs"))
    
    def testQuestionnaire2(self):
        inst = self.instantiate_from("questionnaire-example-f201-lifelines.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire2(inst)
        
        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire2(inst2)
    
    def implQuestionnaire2(self, inst):
        self.assertEqual(force_bytes(inst.code[0].code), force_bytes("VL 1-1, 18-65_1.2.2"))
        self.assertEqual(force_bytes(inst.code[0].display), force_bytes("Lifelines Questionnaire 1 part 1"))
        self.assertEqual(force_bytes(inst.code[0].system), force_bytes("http://example.org/system/code/lifelines/nl"))
        self.assertEqual(inst.date.date, FHIRDate("2010").date)
        self.assertEqual(inst.date.as_json(), "2010")
        self.assertEqual(force_bytes(inst.id), force_bytes("f201"))
        self.assertEqual(force_bytes(inst.item[0].linkId), force_bytes("1"))
        self.assertEqual(force_bytes(inst.item[0].text), force_bytes("Do you have allergies?"))
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("boolean"))
        self.assertEqual(force_bytes(inst.item[1].item[0].linkId), force_bytes("2.1"))
        self.assertEqual(force_bytes(inst.item[1].item[0].text), force_bytes("What is your gender?"))
        self.assertEqual(force_bytes(inst.item[1].item[0].type), force_bytes("string"))
        self.assertEqual(force_bytes(inst.item[1].item[1].linkId), force_bytes("2.2"))
        self.assertEqual(force_bytes(inst.item[1].item[1].text), force_bytes("What is your date of birth?"))
        self.assertEqual(force_bytes(inst.item[1].item[1].type), force_bytes("date"))
        self.assertEqual(force_bytes(inst.item[1].item[2].linkId), force_bytes("2.3"))
        self.assertEqual(force_bytes(inst.item[1].item[2].text), force_bytes("What is your country of birth?"))
        self.assertEqual(force_bytes(inst.item[1].item[2].type), force_bytes("string"))
        self.assertEqual(force_bytes(inst.item[1].item[3].linkId), force_bytes("2.4"))
        self.assertEqual(force_bytes(inst.item[1].item[3].text), force_bytes("What is your marital status?"))
        self.assertEqual(force_bytes(inst.item[1].item[3].type), force_bytes("string"))
        self.assertEqual(force_bytes(inst.item[1].linkId), force_bytes("2"))
        self.assertEqual(force_bytes(inst.item[1].text), force_bytes("General questions"))
        self.assertEqual(force_bytes(inst.item[1].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.item[2].item[0].linkId), force_bytes("3.1"))
        self.assertEqual(force_bytes(inst.item[2].item[0].text), force_bytes("Do you smoke?"))
        self.assertEqual(force_bytes(inst.item[2].item[0].type), force_bytes("boolean"))
        self.assertEqual(force_bytes(inst.item[2].item[1].linkId), force_bytes("3.2"))
        self.assertEqual(force_bytes(inst.item[2].item[1].text), force_bytes("Do you drink alchohol?"))
        self.assertEqual(force_bytes(inst.item[2].item[1].type), force_bytes("boolean"))
        self.assertEqual(force_bytes(inst.item[2].linkId), force_bytes("3"))
        self.assertEqual(force_bytes(inst.item[2].text), force_bytes("Intoxications"))
        self.assertEqual(force_bytes(inst.item[2].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.subjectType[0]), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/Questionnaire/f201"))
    
    def testQuestionnaire3(self):
        inst = self.instantiate_from("questionnaire-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire3(inst)
        
        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire3(inst2)
    
    def implQuestionnaire3(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2012-01").date)
        self.assertEqual(inst.date.as_json(), "2012-01")
        self.assertEqual(force_bytes(inst.id), force_bytes("3141"))
        self.assertEqual(force_bytes(inst.item[0].code[0].code), force_bytes("COMORBIDITY"))
        self.assertEqual(force_bytes(inst.item[0].code[0].system), force_bytes("http://example.org/system/code/sections"))
        self.assertEqual(force_bytes(inst.item[0].item[0].code[0].code), force_bytes("COMORB"))
        self.assertEqual(force_bytes(inst.item[0].item[0].code[0].system), force_bytes("http://example.org/system/code/questions"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].code[0].code), force_bytes("CARDIAL"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].code[0].system), force_bytes("http://example.org/system/code/sections"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].enableWhen[0].answerCoding.code), force_bytes("Y"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].enableWhen[0].answerCoding.system), force_bytes("http://hl7.org/fhir/v2/0136"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].enableWhen[0].question), force_bytes("1.1"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].code[0].code), force_bytes("COMORBCAR"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].code[0].system), force_bytes("http://example.org/system/code/questions"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].item[0].code[0].code), force_bytes("COMCAR00"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].item[0].code[0].display), force_bytes("Angina Pectoris"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].item[0].code[0].system), force_bytes("http://example.org/system/code/questions"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].item[0].code[1].code), force_bytes("194828000"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].item[0].code[1].display), force_bytes("Angina (disorder)"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].item[0].code[1].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].item[0].linkId), force_bytes("1.1.1.1.1"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].item[0].prefix), force_bytes("1.1.1"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].item[0].type), force_bytes("choice"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].item[1].code[0].code), force_bytes("22298006"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].item[1].code[0].display), force_bytes("Myocardial infarction (disorder)"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].item[1].code[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].item[1].linkId), force_bytes("1.1.1.1.2"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].item[1].prefix), force_bytes("1.1.2"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].item[1].type), force_bytes("choice"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].linkId), force_bytes("1.1.1.1"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].prefix), force_bytes("1.1"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[0].type), force_bytes("choice"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[1].code[0].code), force_bytes("COMORBVAS"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[1].code[0].system), force_bytes("http://example.org/system/code/questions"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[1].linkId), force_bytes("1.1.1.2"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[1].prefix), force_bytes("1.2"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].item[1].type), force_bytes("choice"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].linkId), force_bytes("1.1.1"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.item[0].item[0].linkId), force_bytes("1.1"))
        self.assertEqual(force_bytes(inst.item[0].item[0].prefix), force_bytes("1"))
        self.assertEqual(force_bytes(inst.item[0].item[0].type), force_bytes("choice"))
        self.assertEqual(force_bytes(inst.item[0].linkId), force_bytes("1"))
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.item[1].code[0].code), force_bytes("HISTOPATHOLOGY"))
        self.assertEqual(force_bytes(inst.item[1].code[0].system), force_bytes("http://example.org/system/code/sections"))
        self.assertEqual(force_bytes(inst.item[1].item[0].code[0].code), force_bytes("ABDOMINAL"))
        self.assertEqual(force_bytes(inst.item[1].item[0].code[0].system), force_bytes("http://example.org/system/code/sections"))
        self.assertEqual(force_bytes(inst.item[1].item[0].item[0].code[0].code), force_bytes("STADPT"))
        self.assertEqual(force_bytes(inst.item[1].item[0].item[0].code[0].display), force_bytes("pT category"))
        self.assertEqual(force_bytes(inst.item[1].item[0].item[0].code[0].system), force_bytes("http://example.org/system/code/questions"))
        self.assertEqual(force_bytes(inst.item[1].item[0].item[0].linkId), force_bytes("2.1.2"))
        self.assertEqual(force_bytes(inst.item[1].item[0].item[0].type), force_bytes("choice"))
        self.assertEqual(force_bytes(inst.item[1].item[0].linkId), force_bytes("2.1"))
        self.assertEqual(force_bytes(inst.item[1].item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.item[1].linkId), force_bytes("2"))
        self.assertEqual(force_bytes(inst.item[1].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.subjectType[0]), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Cancer Quality Forum Questionnaire 2012"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/Questionnaire/3141"))
    
    def testQuestionnaire4(self):
        inst = self.instantiate_from("questionnaire-example-bluebook.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire4(inst)
        
        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire4(inst2)
    
    def implQuestionnaire4(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2013-02-19").date)
        self.assertEqual(inst.date.as_json(), "2013-02-19")
        self.assertEqual(force_bytes(inst.id), force_bytes("bb"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].linkId), force_bytes("nameOfChild"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].text), force_bytes("Name of child"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[0].type), force_bytes("string"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[1].linkId), force_bytes("sex"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[1].option[0].valueCoding.code), force_bytes("F"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[1].option[1].valueCoding.code), force_bytes("M"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[1].text), force_bytes("Sex"))
        self.assertEqual(force_bytes(inst.item[0].item[0].item[1].type), force_bytes("choice"))
        self.assertEqual(force_bytes(inst.item[0].item[0].linkId), force_bytes("group"))
        self.assertEqual(force_bytes(inst.item[0].item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[0].linkId), force_bytes("birthWeight"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[0].text), force_bytes("Birth weight (kg)"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[0].type), force_bytes("decimal"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[1].linkId), force_bytes("birthLength"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[1].text), force_bytes("Birth length (cm)"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[1].type), force_bytes("decimal"))
        self.assertTrue(inst.item[0].item[1].item[2].item[0].enableWhen[0].hasAnswer)
        self.assertEqual(force_bytes(inst.item[0].item[1].item[2].item[0].enableWhen[0].question), force_bytes("vitaminKgiven"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[2].item[0].item[0].linkId), force_bytes("vitaminiKDose1"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[2].item[0].item[0].text), force_bytes("1st dose"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[2].item[0].item[0].type), force_bytes("dateTime"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[2].item[0].item[1].linkId), force_bytes("vitaminiKDose2"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[2].item[0].item[1].text), force_bytes("2nd dose"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[2].item[0].item[1].type), force_bytes("dateTime"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[2].item[0].linkId), force_bytes("vitaminKgivenDoses"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[2].item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[2].linkId), force_bytes("vitaminKgiven"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[2].option[0].valueCoding.code), force_bytes("INJECTION"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[2].option[1].valueCoding.code), force_bytes("INTRAVENOUS"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[2].option[2].valueCoding.code), force_bytes("ORAL"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[2].text), force_bytes("Vitamin K given"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[2].type), force_bytes("choice"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[3].item[0].linkId), force_bytes("hepBgivenDate"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[3].item[0].text), force_bytes("Date given"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[3].item[0].type), force_bytes("date"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[3].linkId), force_bytes("hepBgiven"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[3].text), force_bytes("Hep B given y / n"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[3].type), force_bytes("boolean"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[4].linkId), force_bytes("abnormalitiesAtBirth"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[4].text), force_bytes("Abnormalities noted at birth"))
        self.assertEqual(force_bytes(inst.item[0].item[1].item[4].type), force_bytes("string"))
        self.assertEqual(force_bytes(inst.item[0].item[1].linkId), force_bytes("neonatalInformation"))
        self.assertEqual(force_bytes(inst.item[0].item[1].text), force_bytes("Neonatal Information"))
        self.assertEqual(force_bytes(inst.item[0].item[1].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.item[0].linkId), force_bytes("birthDetails"))
        self.assertEqual(force_bytes(inst.item[0].text), force_bytes("Birth details - To be completed by health professional"))
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("AU"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("urn:iso:std:iso:3166"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("New South Wales Department of Health"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.subjectType[0]), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("NSW Government My Personal Health Record"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/Questionnaire/bb"))

