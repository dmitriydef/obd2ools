
def linear(data, gain, offset):
	return data * gain + offset

#	0	1	2	3	4	5	6	7
#	[header,	pid,	example,	short name,	units,	format,	func,	[params]],
scanned_pids = [
	[0x7e0,	'221101',	'82',	'COOLAN TEMP/S',	'°С',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221102',	'00',	'VHCL SPEED SE',	'км/час',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221103',	'B1',	'BATTERY VOLT',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221104',	'44',	'FUEL TEMP SEN',	'°С',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221105',	'00',	'EGR TEMP SEN',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221106',	'66',	'INT/A TEMP SE',	'°С',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221107',	'5F',	'IGN TIMING',	'BTDC',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221108',	'5F',	'IGN TIMING',	'BTDC',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221109',	'5F',	'IGN TIMING',	'BTDC',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22110A',	'5F',	'IGN TIMING',	'BTDC',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22110C',	'C8',	'IACV-AAC/V',	'Шаг',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22110D',	'34',	'Базовое значение оборотов ХХ',	'об/мин',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221110',	'00',	'PURG VOL C/V',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221111',	'44',	'FUEL T/TMP SE',	'°С',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221112',	'00',	'EGR VOL CON/V',	'Шаг',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221113',	'00',	'FPCM DR VOLT',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221114',	'34',	'FUEL LEVEL SE',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221115',	'00',	'EVAP SYS PRES',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221116',	'00',	'ABSOL PRES/SE',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221117',	'3A',	'CAL/LD VALUE',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221118',	'00',	'HO2S1 (B1)',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221119',	'00',	'HO2S1 (B2)',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22111A',	'1C',	'HO2S2 (B1)',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22111B',	'1C',	'HO2S2 (B2)',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22111C',	'00',	'THRTL POS SEN',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22111E',	'02',	'ABSOL TH-P/S',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22111F',	'7B',	'ENG OIL TEMP',	'°С',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221121',	'00',	'EX/G TMP S-B1',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221122',	'00',	'EX/G TMP S-B2',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221123',	'65',	'Кратковременная топливная коррекция B1',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221124',	'67',	'Кратковременная топливная коррекция B2',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221125',	'6A',	'Долговременная топливная коррекция B1',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221126',	'6C',	'Долговременная топливная коррекция B2',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221129',	'CF',	'ATOM PRES SEN',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22112A',	'00',	'MAP SENSOR',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22112B',	'80',	'EVAP DIAG STATUS',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22112D',	'00',	'Корректировка УОЗ',	'°',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22112E',	'00',	'Корректировка оборотов ХХ',	'об/мин',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221130',	'00',	'PRESS REG',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221131',	'00',	'FUEL INJ TIM',	'BTDC',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221132',	'00',	'FUEL INJ TIM',	'BTDC',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221133',	'00',	'FUEL INJ TIM',	'BTDC',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221134',	'40',	'A/F RATIO',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221135',	'7F',	'INT/V TIM(B1)',	'°CA',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221136',	'00',	'INT/V TIM(B1)',	'°CA',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221137',	'00',	'INT/V TIM(B2)',	'°CA',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221138',	'00',	'INT/V SOL(B1)',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221139',	'00',	'INT/V SOL(B2)',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22113A',	'80',	'VTC Angel Intake',	'°',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22113B',	'00',	'VTC Angel Intake',	'°',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22113C',	'5F',	'IGN TIMING',	'BTDC',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22113D',	'00',	'FUEL INJ TIM',	'BTDC',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221143',	'00',	'Температура EGR',	'°С',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221144',	'00',	'EVAP DIAG STATUS',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221145',	'01',	'221145',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221146',	'83',	'EVAP SYSTEM CLOSE STATUS',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221147',	'58',	'Ниж. предел кратковременной топливной коррекции B1',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221148',	'70',	'Верх. предел кратковременной топливной коррекции B1',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221149',	'00',	'221149',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22114A',	'00',	'TRGT FAN RPM',	'об/мин',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22114C',	'00',	'HO2S3 (B1)',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22114D',	'00',	'HO2S3 (B2)',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22114E',	'8D',	'A/F S1 HTR(B1)',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22114F',	'A0',	'A/F S1 HTR(B2)',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221150',	'00',	'O2SEN HTR DTY',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221159',	'00',	'221159',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22115A',	'00',	'22115A',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221162',	'00',	'IGN TIMING',	'BTDC',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221163',	'81',	'INT/V TIM(B2)',	'°CA',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221164',	'80',	'EXH/V TIM B1',	'°CA',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221165',	'7F',	'EXH/V TIM B2',	'°CA',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221166',	'80',	'221166',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221174',	'00',	'CO ADJUSTMENT',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221178',	'00',	'FAN DUTY',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221179',	'BB',	'AC EVA TEMP',	'°C',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22117A',	'63',	'AC EVA TARGET',	'°C',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22117B',	'00',	'ALT DUTY',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221201',	'0034',	'ENG SPEED',	'об/мин',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221203',	'0000',	'TRVL AFTER MIL',	'км',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221204',	'00C5',	'MAS A/F SE-B1',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221205',	'00C2',	'MAS A/F SE-B2',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221206',	'0110',	'INJ PULSE-B1',	'мс',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221207',	'0117',	'INJ PULSE-B2',	'мс',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221208',	'1947',	'B/FUEL SCHDL',	'мс',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221209',	'01AA',	'MASS AIRFLOW',	'гр/сек',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22120B',	'0000',	'Код текущей ошибки DTC',	'DTC',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22120C',	'0000',	'FUEL PRES SEN',	'МПа',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22120D',	'0090',	'ACCEL SEN 1',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22120E',	'0090',	'ACCEL SEN 2',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22120F',	'006C',	'TP SEN 1-B1',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221210',	'0069',	'TP SEN 2-B1',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221214',	'0000',	'BRAKE BST PRESS SE 1',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221215',	'0000',	'BRAKE BST PRESS SE 2',	'Вольт',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221218',	'00C9',	'221218',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221219',	'0262',	'I/P PULLY SPD',	'об/мин',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22121A',	'0000',	'VEHICLE SPEED',	'км/ч',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22121B',	'135E',	'Ниж. предел баз. длительности импульса впрыска топлива на ХХ',	'мс',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22121C',	'1B1B',	'Вер. предел баз. длительности импульса впрыска топлива на ХХ',	'мс',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221221',	'0093',	'Нижний порог показаний датчика MAF',	'В',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221222',	'00D1',	'Верхний порог показаний датчика MAF',	'В',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221223',	'00F0',	'AC PRESS SEN',	'В',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221225',	'01B5',	'A/F SEN1 (B1)',	'В',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221226',	'01AE',	'A/F SEN1 (B2)',	'В',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22122A',	'017F',	'VHCL SPEED SE',	'км/ч',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22122B',	'0000',	'SET VHCL SPD',	'км/ч',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22122C',	'0000',	'22122C',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22122D',	'0000',	'VTC DTY IN B1',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22122E',	'0000',	'VTC DTY IN B2',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22122F',	'0000',	'VTC DTY EX B1',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221230',	'0000',	'VTC DTY EX B2',	'%',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221234',	'0000',	'221234',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221235',	'0000',	'221235',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221236',	'0000',	'221236',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221237',	'002E',	'221237',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221238',	'0000',	'221238',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221239',	'0000',	'221239',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22123A',	'0000',	'22123A',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22123B',	'0000',	'22123B',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22123C',	'0000',	'22123C',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22123D',	'0000',	'22123D',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22123E',	'0000',	'22123E',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22123F',	'0000',	'22123F',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221241',	'0000',	'221241',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221243',	'0000',	'221243',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221244',	'002D',	'221244',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221245',	'002D',	'221245',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221246',	'01F7',	'BAT CUR SEN',	'мВ',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221247',	'0004',	'221247',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221248',	'CB2F',	'221248',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221249',	'FFEB',	'A/F ADJ-B1',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22124A',	'FFE7',	'A/F ADJ-B2',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22124B',	'006E',	'TP SEN 1-B2',	'mV',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22124C',	'006D',	'TP SEN 2-B2',	'mV',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221250',	'001C',	'221250',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221301',	'0001',	'SNOW MODE SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221301',	'0001',	'CLSD THL/P SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221301',	'0001',	'CVTC LEARNING',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221301',	'0001',	'221301',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221301',	'0001',	'221301',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221301',	'0001',	'221301',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221301',	'0001',	'HO2S3 MNTR(B2)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221301',	'0001',	'HO2S3 MNTR(B1)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221302',	'053F',	'CLSD THL POS',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221302',	'053F',	'START SIGNAL',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221302',	'053F',	'P/N POSI SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221302',	'053F',	'PW/ST SIGNAL',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221302',	'053F',	'AIR COND SIG',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221302',	'053F',	'LOAD SIGNAL',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221302',	'053F',	'CAN CON VC SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221302',	'053F',	'AMB TEMP SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221303',	'3030',	'Shift Solenoid B',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221303',	'3030',	'Shift Solenoid A',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221303',	'3030',	'A/T Data 2 In',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221303',	'3030',	'A/T Data 1 In',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221303',	'3030',	'HO2S2 MNTR(B2)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221303',	'3030',	'HO2S2 MNTR(B1)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221303',	'3030',	'HO2S1 MNTR(B2)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221303',	'3030',	'HO2S1 MNTR(B1)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221304',	'9090',	'Susp Unload',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221304',	'9090',	'A/C PRESS SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221304',	'9090',	'TCC SWITCH',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221304',	'9090',	'OD SWITCH',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221304',	'9090',	'HEATER FAN SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221304',	'9090',	'CLUTCH P/P SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221304',	'9090',	'SWL CON VC SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221304',	'9090',	'IGNITION SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221305',	'6844',	'COMBUSTION',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221305',	'6844',	'BRAKE SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221305',	'6844',	'REV UNIT DR',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221305',	'6844',	'BOOST VCUM SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221305',	'6844',	'FTVOLNEX',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221305',	'6844',	'A/V LEARN',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221305',	'6844',	'FQCAL',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221306',	'0000',	'VVL S/V-EXH',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221306',	'0000',	'VVL S/V-INT',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221306',	'0000',	'INT/V SOL-B2',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221306',	'0000',	'INT/V SOL-B1',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221306',	'0000',	'VIAS S/V-1',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221306',	'0000',	'VARI DUCT S/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221306',	'0000',	'VARI RESO S/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221306',	'0000',	'SWRL CONT S/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221307',	'0242',	'A/T Data 3 Out',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221307',	'0242',	'Режим ХХ',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221307',	'0242',	'ENGINE MOUNT',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221307',	'0242',	'OD CANCEL S/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221307',	'0242',	'TCC SOL/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221307',	'0242',	'EGRC SOL/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221307',	'0242',	'AIR COND RLY',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221307',	'0242',	'IACV-IDLE/UP',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221308',	'0908',	'FPCM',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221308',	'0908',	'FUEL PUMP',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221308',	'0908',	'VVL S/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221308',	'0908',	'FUEL C/V ENG',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221308',	'0908',	'FUEL C/V CYL',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221308',	'0908',	'EGRC SOL/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221309',	'1000',	'PURG CONT S/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221309',	'1000',	'VENT CONT S/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221309',	'1000',	'PURG CONT S/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221309',	'1000',	'VC/V BYPAS S/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221309',	'1000',	'MAP/BARO SW/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221309',	'1000',	'P/REG CONT/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221309',	'1000',	'221309',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221309',	'1000',	'221309',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130A',	'1010',	'IACV-FICD S/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130A',	'1010',	'AUXI CONT S/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130A',	'1010',	'AIR PUMP RLY',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130A',	'1010',	'AIR/P CNT S/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130A',	'1010',	'THRTL RELAY',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130A',	'1010',	'COLD START/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130A',	'1010',	'HO2S3 HTR (B2)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130A',	'1010',	'HO2S3 HTR (B1)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130B',	'0003',	'HO2S2 HTR (B2)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130B',	'0003',	'HO2S2 HTR (B1)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130B',	'0003',	'HO2S1 HTR (B2)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130B',	'0003',	'HO2S1 HTR (B1)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130B',	'0003',	'COOLING FAN',	'-',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130B',	'0003',	'W/G SOL/V-B2',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130B',	'0003',	'W/G SOL/V-B1',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130C',	'4100',	'SRT STATUS: CATALYST',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130C',	'4100',	'SRT STATUS: HEATED CAT',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130C',	'4100',	'SRT STATUS: EVAP SYSTEM',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130C',	'4100',	'SRT STATUS: S-AIR SYSTEM',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130C',	'4100',	'SRT STATUS: REFRIGERANT',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130C',	'4100',	'SRT STATUS: HO2S',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130C',	'4100',	'SRT STATUS: HO2S HTR',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130C',	'4100',	'SRT STATUS: EGR/VVT SYSTEM',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130D',	'103F',	'MAIN SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130D',	'103F',	'CANCEL SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130D',	'103F',	'RESUME/ACC SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130D',	'103F',	'SET SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130D',	'103F',	'BRAKE SW1',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130D',	'103F',	'BRAKE SW2',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130D',	'103F',	'DIST SW',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130D',	'103F',	'22130D',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130E',	'003F',	'VHCL SPD CUT',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130E',	'003F',	'LO SPEED CUT',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130E',	'003F',	'CRUISE LAMP',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130E',	'003F',	'AT OD MONITOR',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130E',	'003F',	'AT OD CANCEL',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130E',	'003F',	'SET LAMP',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130E',	'003F',	'22130E',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130E',	'003F',	'22130E',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130F',	'DBFF',	'Initial Diagnostic',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130F',	'DBFF',	'Transmit Diagnostic',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130F',	'DBFF',	'TCM',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130F',	'DBFF',	'VDC/TCS/ABS',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130F',	'DBFF',	'Meter/M and A',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130F',	'DBFF',	'ICC',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130F',	'DBFF',	'BCM/SEC',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22130F',	'DBFF',	'IPDM E/R',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221310',	'0003',	'221310',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221310',	'0003',	'221310',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221310',	'0003',	'221310',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221310',	'0003',	'221310',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221310',	'0003',	'221310',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221310',	'0003',	'221310',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221310',	'0003',	'221310',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221311',	'0018',	'221311',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221311',	'0018',	'SCB/V CON S/V',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221311',	'0018',	'VT CONT LEARN',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221311',	'0018',	'221311',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221311',	'0018',	'EXH V/T LEARN',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221311',	'0018',	'221311',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221311',	'0018',	'221311',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221311',	'0018',	'221311',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221311',	'0018',	'221311',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221313',	'0008',	'COOLING FAN',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221313',	'0008',	'ALT DUTY SIG',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221313',	'0008',	'VIAS S/V-2',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221313',	'0008',	'221313',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221313',	'0008',	'221313',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221313',	'0008',	'221313',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221315',	'0000',	'221315',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221315',	'0000',	'221315',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221315',	'0000',	'221315',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221315',	'0000',	'221315',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221315',	'0000',	'221315',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221315',	'0000',	'ENG F/C RQST',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221315',	'0000',	'ENG IDLE RQST',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221315',	'0000',	'ENG START RQST',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221502',	'0000',	'221502',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221502',	'0000',	'221502',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221502',	'0000',	'221502',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221502',	'0000',	'221502',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221502',	'0000',	'221502',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221502',	'0000',	'221502',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221502',	'0000',	'221502',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221502',	'0000',	'221502',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221503',	'0000',	'221503',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221503',	'0000',	'221503',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221503',	'0000',	'221503',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221503',	'0000',	'221503',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221503',	'0000',	'221503',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221503',	'0000',	'221503',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221503',	'0000',	'221503',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221503',	'0000',	'221503',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221504',	'0000',	'HO2 S2 DIAG2(B1)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221504',	'0000',	'HO2 S2 DIAG2(B2)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221504',	'0000',	'221504',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221504',	'0000',	'221504',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221504',	'0000',	'221504',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221504',	'0000',	'221504',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221504',	'0000',	'HO2 S2 DIAG1(B1)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221504',	'0000',	'HO2 S2 DIAG1(B2)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221505',	'0000',	'221505',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221505',	'0000',	'221505',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221505',	'0000',	'221505',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221505',	'0000',	'221505',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221505',	'0000',	'221505',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221505',	'0000',	'221505',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221505',	'0000',	'221505',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221505',	'0000',	'221505',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221506',	'0000',	'221506',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221506',	'0000',	'221506',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221506',	'0000',	'221506',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221506',	'0000',	'221506',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221506',	'0000',	'221506',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221506',	'0000',	'221506',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221506',	'0000',	'221506',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221506',	'0000',	'221506',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221507',	'0000',	'221507',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221507',	'0000',	'221507',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221507',	'0000',	'221507',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221507',	'0000',	'221507',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221507',	'0000',	'221507',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221507',	'0000',	'221507',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221507',	'0000',	'221507',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221507',	'0000',	'221507',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221508',	'0000',	'221508',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221508',	'0000',	'221508',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221508',	'0000',	'221508',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221508',	'0000',	'221508',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221508',	'0000',	'221508',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221508',	'0000',	'221508',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221508',	'0000',	'221508',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221508',	'0000',	'221508',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221509',	'0000',	'221509',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221509',	'0000',	'221509',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221509',	'0000',	'221509',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221509',	'0000',	'221509',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221509',	'0000',	'221509',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221509',	'0000',	'221509',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221509',	'0000',	'EVAP DIAG READY',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221509',	'0000',	'EVAP LEAK DIAG',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150A',	'0000',	'22150A',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150A',	'0000',	'22150A',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150A',	'0000',	'22150A',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150A',	'0000',	'22150A',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150A',	'0000',	'22150A',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150A',	'0000',	'22150A',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150A',	'0000',	'22150A',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150A',	'0000',	'22150A',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150B',	'0000',	'22150B',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150B',	'0000',	'22150B',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150B',	'0000',	'22150B',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150B',	'0000',	'22150B',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150B',	'0000',	'22150B',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150B',	'0000',	'22150B',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150B',	'0000',	'22150B',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150B',	'0000',	'22150B',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150C',	'0000',	'22150C',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150C',	'0000',	'22150C',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150C',	'0000',	'22150C',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150C',	'0000',	'22150C',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150C',	'0000',	'22150C',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150C',	'0000',	'22150C',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150C',	'0000',	'22150C',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150C',	'0000',	'22150C',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150D',	'0000',	'22150D',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150D',	'0000',	'22150D',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150D',	'0000',	'A/F SEN1 DIAG2(B1)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150D',	'0000',	'A/F SEN1 DIAG2(B2)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150D',	'0000',	'A/F SEN1 DIAG1(B1)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150D',	'0000',	'A/F SEN1 DIAG1(B2)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150D',	'0000',	'22150D',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150D',	'0000',	'22150D',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150E',	'0000',	'22150E',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150E',	'0000',	'22150E',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150E',	'0000',	'22150E',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150E',	'0000',	'22150E',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150E',	'0000',	'22150E',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150E',	'0000',	'22150E',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150E',	'0000',	'22150E',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150E',	'0000',	'22150E',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150F',	'0000',	'22150F',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150F',	'0000',	'22150F',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150F',	'0000',	'22150F',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150F',	'0000',	'22150F',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150F',	'0000',	'22150F',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150F',	'0000',	'22150F',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150F',	'0000',	'22150F',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'22150F',	'0000',	'22150F',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221510',	'0000',	'221510',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221510',	'0000',	'221510',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221510',	'0000',	'221510',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221510',	'0000',	'221510',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221510',	'0000',	'221510',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221510',	'0000',	'221510',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221510',	'0000',	'221510',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221510',	'0000',	'221510',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221511',	'0000',	'221511',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221511',	'0000',	'221511',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221511',	'0000',	'221511',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221511',	'0000',	'221511',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221511',	'0000',	'221511',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221511',	'0000',	'221511',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221511',	'0000',	'221511',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221511',	'0000',	'221511',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221512',	'7000',	'221512',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221512',	'7000',	'221512',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221512',	'7000',	'221512',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221512',	'7000',	'221512',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221512',	'7000',	'221512',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221512',	'7000',	'221512',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221512',	'7000',	'221512',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221512',	'7000',	'221512',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221513',	'0000',	'221513',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221513',	'0000',	'221513',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221513',	'0000',	'A/F SEN1 DIAG3(B1)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221513',	'0000',	'A/F SEN1 DIAG3(B2)',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221513',	'0000',	'221513',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221513',	'0000',	'221513',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221513',	'0000',	'221513',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221513',	'0000',	'221513',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221514',	'0000',	'221514',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221514',	'0000',	'221514',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221514',	'0000',	'221514',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221514',	'0000',	'221514',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221514',	'0000',	'221514',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221514',	'0000',	'221514',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221514',	'0000',	'ENG START DIAG',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221514',	'0000',	'221514',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221515',	'0000',	'221515',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221515',	'0000',	'221515',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221515',	'0000',	'221515',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221515',	'0000',	'221515',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221515',	'0000',	'221515',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221515',	'0000',	'221515',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221515',	'0000',	'ENG ST DIAG RSLT',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221515',	'0000',	'221515',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221516',	'0000',	'221516',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221516',	'0000',	'221516',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221516',	'0000',	'221516',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221516',	'0000',	'221516',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221516',	'0000',	'221516',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221516',	'0000',	'221516',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221516',	'0000',	'221516',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221516',	'0000',	'221516',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221517',	'0000',	'221517',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221517',	'0000',	'VVEL LEARN',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221517',	'0000',	'221517',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221517',	'0000',	'221517',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221517',	'0000',	'221517',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221517',	'0000',	'221517',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221517',	'0000',	'221517',	'Бит',	'0.3f',	linear,	[0.0,	0]],
	[0x7e0,	'221517',	'0000',	'221517',	'Бит',	'0.3f',	linear,	[0.0,	0]],
]
