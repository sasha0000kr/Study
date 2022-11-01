--pid--
kp = 0
ki = 0
kd = 0

--Входные значения регулятора--
set_point = 0          --Заданное значение
input = sim.Read()    --Чтение значений с датчика

--Обработка времени работы--
start_time = sim.getTime()
get_time = sim.getTime()

function pin (kp, ki, kd, start_time, get_time set_point, input)
    --Объявление переменных--
    local I = 0 
    local prev_err = 0

    --Вычисление времени работы--
    local dt = start_time - get_time

    --Реализация вычислений--
    P = (set_point - input) 
    I = I + (set_point - input) * dt

    err = set_point - input
    D = (err - prev_err) / dt
    prev_err = err

    return (P*kp + I*ki + D*kd)