try:
    import pandas
    print("Hello world")

except ModuleNotFoundError:
    print(f"Ye Module  to h ni")
except Exception as e:
    print(f"{e}")
else:
    print("try is Successful")
