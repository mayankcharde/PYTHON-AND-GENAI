def serve_chai(flavour):
    try:
        print(f"preparing {flavour} chai")
        if flavour == "unknown":
            raise ValueError("we dont have ")
    except ValueError as e:
        print("error", e)
    else:
        print(f"{flavour} chai is served")
    finally:
        print("next customer please")
        
serve_chai("masala")
serve_chai("unknown")                