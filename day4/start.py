# import fun1
import pakiet
from pakiet import fun
import pakiet.fun as pk

# fun1.dodaj2(10, 20)
fun.powitanie()
pk.powitanie()

# po dodaniu w __init__.py odpowiedniego importu funkcja jest widoczna poprzez pakiet
pakiet.powitanie()  # Powitanie z pliku 'fun2' pakietu 'pakiet'
# pakiet.fun2
# Cześć
# Cześć
# Powitanie z pliku 'fun2' pakietu 'pakiet'
