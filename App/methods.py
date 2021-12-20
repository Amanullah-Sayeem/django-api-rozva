def deleteMethod(modalName, id):
    query = modalName.objects.filter(id=id)
    temp = query.delete()
    return (temp, "deleted succes ky")


def postMethod(modalName, object):
    print("sasasasa===", modalName.__doc__)
