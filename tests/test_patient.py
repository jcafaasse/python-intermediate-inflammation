"""Tests for the Patient model."""

from inflammation.models import Patient
import numpy.testing as npt

def test_create_patient():

    name = 'Alice'
    weight = 60
    height= 1.6
    patient = Patient(name=name, weight=weight, height=height)

    assert patient.name == name
    assert patient.weight == weight
    assert patient.height == height

def test_get_body_mass_index():
    name = "Alice"
    weight = 60
    height = 1.6
    patient = Patient(name=name, weight=weight, height=height)
    expected_body_mass_index = 23.4375

    npt.assert_almost_equal(patient.get_body_mass_index(), expected_body_mass_index)
    
