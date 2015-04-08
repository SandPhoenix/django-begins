from django import template
from roman import toRoman

register = template.Library()
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

def romanize_filter(value, args=None):
	"""Change int or long into Roman Numeral all other types are passed out
	You can add an argument like this:
		...
		{{ object.id|romanize:"upper" }}
		...
	For upper case roman numerals. The tag defaults to lowercase numerals for
	no good reason other than I prefer the look of them."""
	if isinstance(value, int) or isinstance(value, long):
		if args != None:
			if args.lower() == "upper":
				return toRoman(value)
			else:
				return toRoman(value).lower()
		else:
			return toRoman(value).lower()
	else:
		return value
register.filter('romanize', romanize_filter)
register.filter('addstr',addstr)