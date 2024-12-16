### 1.Especificación do contorna de tarefas
Contorno de tarefas | Observable| Axentes | Determinista | Episódico | Estático | Discreto | Coñecido
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
 RPS | Parcialmnete | Multi | Determinista | Secuencial | Estático | Discreto  |  Conocido |

Parcialmente observable: No podemos saber con certeza que va a sacar el otro jugador.

Multiagente: hay un agente máquina y un agente humano.

Determinista: Dependiendo de cual sea la jugada que más haya usado el agente humano en una cantidad determinada de partidas, el agente máquina deduce cual puede ser la siguiente acción del humano. Por tanto, las acciones de la máquina están determinadas por las del humano.

Secuencial: Las acciones del jugador influirán en las futuras de la máquina.

Estático: El entorno no cambia con el paso del tiempo.

Discreto: El piedra, papel, tijeras solo tiene tres estados distintos.

Conocido: Ambos agentes conocen las reglas del juego.