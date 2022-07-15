"""Tests for the Patient model."""
import pytest
import numpy.testing as npt


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name

@pytest.mark.parametrize(
    "test, expected",
    [
        (
            [[0,1]],
            [[0,1]]
        ),
        (
            [[0,1], [None,4]],
            [[0,1], [1,4]]
        ),

])

def test_add_patient_observation(test, expected):
    from inflammation.models import Patient
    from inflammation.models import Observation

    name = 'Alice'
    p = Patient(name=name)
    for t in test:
        p.add_observation(t[1], day=t[0])
    for i,p in enumerate(p.observations):
        assert isinstance(p, Observation)
        npt.assert_equal(p.day, expected[i][0])
        npt.assert_equal(p.value, expected[i][1])



def test_no_duplicate_patients():
    """Check adding the same patient to the same doctor twice does not result in duplicates. """
    from inflammation.models import Doctor, Patient
    doc = Doctor("Sheila Wheels")
    alice = Patient("Alice")
    doc.add_patient(alice)
    doc.add_patient(alice)
    npt.assert_equal(len(doc.patients), 1)


def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Dr. White'
    d = Doctor(name=name)

    npt.assert_equal(d.name,name)


def test_add_doctor_patient():
    from inflammation.models import Doctor
    from inflammation.models import Patient
    from inflammation.models import Person
    name = 'Dr. White'
    d = Doctor(name=name)
    name = 'Alice'
    p = Patient(name=name)
    d.add_patients(p)

    assert p in d.patients
    for p in d.patients:
        assert isinstance(p, Person)

