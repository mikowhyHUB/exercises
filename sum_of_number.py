print('Printing current and previous number sum in a range(10)')
pnumb = 0
for cnumb in range(10):
    x = pnumb + cnumb
    print("Current number", cnumb, "Previous number",
          pnumb, "Sum", pnumb + cnumb)
    pnumb = cnumb
