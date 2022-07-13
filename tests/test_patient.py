"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name


def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Dr. White'
    d = Doctor(name=name)

    assert d.name == name


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

