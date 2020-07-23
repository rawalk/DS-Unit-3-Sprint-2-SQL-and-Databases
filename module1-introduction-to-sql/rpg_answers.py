import sqlite3
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

def question_1():
    '''
    How many total Characters are there?
    '''
    query = 'SELECT COUNT(*) FROM charactercreator_character'
    # fetch one because it's a tidier output than the ()'s of fetchall
    result = curs.execute(query).fetchone()
    print('How many total Characters are there?', result[0])


def question_2():
    '''
    How many of each specific subclass?
    '''
    query = 'SELECT(SELECT COUNT(*) \
             FROM charactercreator_cleric) AS cleric_count, \
            (SELECT COUNT(*) \
            FROM charactercreator_mage) AS mage_count, \
            (SELECT COUNT(*) \
            FROM charactercreator_necromancer) AS necro_count, \
            (SELECT COUNT(*) \
            FROM charactercreator_fighter) AS fighter_count, \
            (SELECT COUNT(*) \
            FROM charactercreator_thief) AS thief_count;'
    print('\nHow many of each specific subclass?')
    print(pd.read_sql(query, conn).T.rename(columns={0: 'Count'}))


def question_3():
    '''
    How many total Items?
    '''
    query = 'SELECT COUNT(*) FROM armory_item;'
    # fetch one because it's a tidier output than the ()'s of fetchall
    result = curs.execute(query).fetchone()
    print('\nHow many total Items?', result[0])


def question_4():
    '''
    How many of the Items are weapons? How many are not?
    '''
    query = 'SELECT COUNT(*) FROM armory_weapon;'
    weapons_c = curs.execute(query).fetchone()
    print('\nHow many of the items are are weapons?', weapons_c[0])
    query = 'SELECT COUNT(*) FROM armory_item;'
    item_c = curs.execute(query).fetchone()
    print('\nHow many are not?', item_c[0]-weapons_c[0])


def question_5():
    '''
    How many Items does each character have? (Return first 20 rows)
    '''
    query = 'SELECT COUNT(*), character_id \
             FROM charactercreator_character_inventory \
             GROUP BY character_id LIMIT 20;'
    print('\nHow many items does each character have? (first 20 rows):')
    result = pd.read_sql(query, conn)
    result = result.set_index('character_id')
    # for a tidier output. 
    print(result.T)


def question_6():
    '''
    How many Weapons does each character have? (Return first 20 rows)
    '''
    query = 'SELECT COUNT(*), character_id \
             FROM charactercreator_character_inventory AS cci, \
                  armory_weapon AS aw \
             WHERE cci.item_id = aw.item_ptr_id \
             GROUP BY character_id LIMIT 20;'
    result = pd.read_sql(query, conn)
    result = result.set_index('character_id')
    print('\nHow many weapons does each character have? (first 20 rows):')
    # for a tidier output. 
    print(result.T)


def question_7():
    '''
    On average, how many Items does each Character have?
    '''
    query = 'SELECT AVG(items.count) FROM ( \
                SELECT COUNT(*) as count, character_id \
                FROM charactercreator_character_inventory \
                GROUP BY character_id) AS items;'
    # fetch one because it's a tidier output than the ()'s of fetchall
    result = curs.execute(query).fetchone()
    print('\nOn average, how many Items does each Character have?', round(result[0],5))


def question_8():
    '''
    On average, how many Weapons does each character have?
    '''
    query = 'SELECT AVG(weapons.count) FROM ( \
                SELECT COUNT(*) as count \
                FROM charactercreator_character_inventory AS cci, \
                     armory_weapon AS aw \
                WHERE cci.item_id = aw.item_ptr_id \
                GROUP BY character_id) as weapons'
    result = curs.execute(query).fetchone()
    print('\nOn average, how many Weapons does each character have?', result[0])

#executing the answer to the following questions: 
question_1()
question_2()
question_3()
question_4()
question_5()
question_6()
question_7()
question_8()