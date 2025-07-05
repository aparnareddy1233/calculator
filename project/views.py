from django.shortcuts import render

def index(request):
    result = None

    if request.method == 'POST':
        try:
            num1 = float(request.POST['num1'])
            num2 = float(request.POST['num2'])
            op = request.POST['op']

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2 if num2 != 0 else 'Error: Divide by zero'
            else:
                result = 'Invalid operation'
        except ValueError:
            result = 'Invalid input'

    return render(request, 'index.html', {'result': result})
