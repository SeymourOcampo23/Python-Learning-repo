def make_profile(name, **info):
   if "age" in info:
       age = info.get("age")
       print(f"{name} is {age} years old. ")
   else:
       print(f"{name} is unknown years old. ")

make_profile("mike", age=23, height=1.70, weight=160)
make_profile("Ana")
make_profile("Jim", job="Python Developer")


def make_dino(name, **info):
    profile = {"dino_type": name}
    profile.update(info) #will add the kwargs into the dictionary called "profile"
    return profile


print(make_dino("Stegasaurus", height=2.3, length=3.2, type="herbivore"))
print(make_dino("T-Rex")) # Empty info dictionary because there are no kwarg parameters.


# Looping over kwargs

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(type="Carnivore", is_small = True, height=11, weight=10000, intelligence="high")

def show_settings(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")

show_settings(theme="Dark", brightness=89, resolution=1080)



try:
    print(make_profile()) #Missing positional argument name. 
except TypeError as e:
    print(e)

def describe(a, *args, sep=",", **kwargs): #order of arguments
    print(f"a: {a}")
    print(f"args: {args}")
    print(f"sep: {sep}")
    print(f"kwargs: {kwargs}")

describe("Chicken")
describe("Chicken", 85, sep=23)
describe(1, 2, 3, balance=99)


def build_request(model, temperature=0.7, **options): #flat dictionary
    info = {"model": model, "temperature": temperature}
    info.update(options)
    return info

def alt_build_request(model, **options):#the key "option" is nested
    options.setdefault("temperature", 0.7)
    return {"model": model, "options": options}

print(build_request("my-model", max_tokens=100))
print(alt_build_request("my-model", max_tokens=1000))



