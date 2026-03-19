from django import template

register = template.Library()


@register.filter(name='times')
def times(number):
    """
    Returns a range of numbers from 0 to number-1.
    Usage: {% for i in rating|times %}...{% endfor %}
    """
    try:
        return range(int(number))
    except (ValueError, TypeError):
        return range(0)


@register.filter(name='neg_times')
def neg_times(number, max_value):
    """
    Returns a range of numbers from 0 to (max_value - number - 1).
    Usage: {% for i in rating|neg_times:5 %}...{% endfor %}
    Used to display empty stars.
    """
    try:
        return range(max_value - int(number))
    except (ValueError, TypeError):
        return range(0)


@register.filter(name='format_vnd')
def format_vnd(value):
    """
    Format giá trị thành tiền Việt Nam Đồng.
    Ví dụ: 150000 -> 150.000đ
    """
    try:
        value = int(value)
        return f"{value:,}đ".replace(",", ".")
    except (ValueError, TypeError):
        return "0đ"