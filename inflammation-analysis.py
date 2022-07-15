"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse
from inflammation import views, models


def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    InFiles = args.infiles
    if not isinstance(InFiles, list):
        InFiles = [args.infiles]


    if args.view == 'visualize':
        for filename in InFiles:
            inflammation_data = models.load_csv(filename)

            view_data = {'average': models.daily_mean(inflammation_data),
                     'max': models.daily_max(inflammation_data),
                     'min': models.daily_min(inflammation_data)}


            views.visualize(view_data)
    elif args.view == 'record':
        if args.patient is not None:
            for filename in InFiles:
                p = models.Patient(models.Person("UNKNOWN"))
                inflammation_data = models.load_csv(filename)
                for o in inflammation_data[int(args.patient)]:
                    p.add_observation(value=o)

            views.display_patient_record(p)
        else:
            print("provide a patient number")
    else:
        print("available view options are 'visualize' for a plot and 'record' for printed output")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    parser.add_argument(
        '--view',
        default='visualize',
        choices=['visualize', 'record'],
        help='Which view should be used?')

    parser.add_argument(
        '--patient',
        type=int,
        default=0,
        help='Which patient should be displayed?')

    args = parser.parse_args()


    main(args)
