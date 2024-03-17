-- Создание таблицы СУДНО
CREATE TABLE СУДНО (
    ИДЕНТИФИКАТОР CHAR(3) PRIMARY KEY,
    НАЗВАНИЕ TEXT NOT NULL,
    ПОРТ_ПРИПИСКИ TEXT NOT NULL,
    ЛЬГОТА INT NOT NULL 
);

-- Создание таблицы МЕСТА_ПОГРУЗКИ
CREATE TABLE МЕСТА_ПОГРУЗКИ (
    ИДЕНТИФИКАТОР CHAR(3) PRIMARY KEY,
    ПРИЧАЛ TEXT NOT NULL,
    ПОРТ TEXT NOT NULL,
    ОТЧИСЛЕНИЯ_НА_ПОГРУЗКУ INT NOT NULL,
	ДАТА DATE NOT NULL
);

-- Создание таблицы ГРУЗ
CREATE TABLE ГРУЗ (
    ИДЕНТИФИКАТОР CHAR(3) PRIMARY KEY,
    НАЗВАНИЕ TEXT NOT NULL,
    ПОРТ_СКЛАДИРОВАНИЯ TEXT NOT NULL,
    СТОИМОСТЬ NUMERIC NOT NULL,
    МАКС_КОЛ_ВО INT NOT NULL
);
CREATE TYPE mood AS ENUM('ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС'); 
-- Создание таблицы ПОГРУЗКА
CREATE TABLE ПОГРУЗКА (
    НОМЕР_ВЕДОМОСТИ CHAR(5) PRIMARY KEY,
    ДАТА mood NOT NULL,
    СУДНО CHAR(3),
    МЕСТО_ПОГРУЗКИ CHAR(3),
    ГРУЗ CHAR(3),
    КОЛ_ВО INT NOT NULL,
    СТОИМОСТЬ NUMERIC NOT NULL,
    FOREIGN KEY (СУДНО) REFERENCES СУДНО(ИДЕНТИФИКАТОР),
    FOREIGN KEY (МЕСТО_ПОГРУЗКИ) REFERENCES МЕСТА_ПОГРУЗКИ(ИДЕНТИФИКАТОР),
    FOREIGN KEY (ГРУЗ) REFERENCES ГРУЗ(ИДЕНТИФИКАТОР)
);
