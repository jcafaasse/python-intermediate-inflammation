#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse
import os

from inflammation import models, views, analysis


def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    inflammation_files = args.infiles
    if not isinstance(inflammation_files, list):
        inflammation_files = [args.infiles]

    for filename in inflammation_files:
        inflammation_data = models.load_csv(filename)

        view_data = {
            "average": models.daily_mean(inflammation_data),
            "max": models.daily_max(inflammation_data),
            "min": models.daily_min(inflammation_data),
        }
        if args.output_dir:
            views.visualize(
                view_data,
                filename=os.path.basename(filename),
                output_dir=args.output_dir,
            )
        else:
            views.visualize(view_data)

    data_dir = os.path.dirname(inflammation_files[0])
    _, extension = os.path.splitext(inflammation_files[0])
    if extension == ".csv":
        data_source = analysis.CSVDataSource(data_dir)
    elif extension == ".json":
        data_source = analysis.JSONDataSource(data_dir)
    data = data_source.load_inflammation_data()
    print(models.daily_max(data))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A basic patient inflammation data management system"
    )

    parser.add_argument(
        "infiles",
        nargs="+",
        help="Input CSV(s) containing inflammation series for each patient",
    )

    parser.add_argument("-output_dir", help="Output directory to save figures as PNG")

    args = parser.parse_args()

    main(args)
