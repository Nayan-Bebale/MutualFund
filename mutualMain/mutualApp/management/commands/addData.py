import csv
from django.core.management.base import BaseCommand
from mutualApp.models import MainDataSet, SelectedData  # Import models from the current app

# Function to import data from MF_India_AI.csv
class Command(BaseCommand):
    def handle(self, *args, **options):
        csv_file1_path = 'D:/MutualFund/mutualMain/mutualApp/MF_India_AI.csv'
        csv_file2_path = 'D:/MutualFund/mutualMain/mutualApp/selectedFeatures.csv'

        def import_main_data():
            with open(csv_file1_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        returns_5yr = float(row['returns_5yr'])
                    except ValueError:
                        returns_5yr = 0.0  # Provide a default value or skip the row if necessary
                    
                    try:
                        returns_3yr = float(row['returns_3yr'])
                    except ValueError:
                        returns_3yr = 0.0  # Provide a default value or skip the row if necessary
                        
                    try:
                        returns_1yr = float(row['returns_1yr'])
                    except ValueError:
                        returns_1yr = 0.0  # Provide a default value or skip the row if necessary
                        
                    MainDataSet.objects.create(
                        scheme_name=row['scheme_name'],
                        min_sip=int(row['min_sip']),
                        min_lumpsum=int(row['min_lumpsum']),
                        expense_ratio=float(row['expense_ratio']),
                        fund_size_cr=float(row['fund_size_cr']),
                        fund_age_yr=int(row['fund_age_yr']),
                        risk_level=int(row['risk_level']),
                        rating=int(row['rating']),
                        category=row['category'],
                        sub_category=row['sub_category'],
                        returns_1yr=returns_1yr,
                        returns_3yr=returns_3yr,
                        returns_5yr=returns_5yr
                    )



        # Function to import data from selectedFeatures.csv
        def import_selected_data():
            with open(csv_file2_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    SelectedData.objects.create(
                        scheme_name=row['scheme_name'],
                        risk_level=int(row['risk_level']),
                        risk_category=row['risk_category'],
                        returns_1yr=float(row['returns_1yr']),
                        returns_3yr=float(row['returns_3yr']),
                        returns_5yr=float(row['returns_5yr'])
                    )

        # Call the functions to import data
        import_main_data()
        import_selected_data()
