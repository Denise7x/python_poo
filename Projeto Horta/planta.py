import sqlite3

class Planta:
    def __init__(self, db_name="horta_db.sqlite"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS plantas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    data_plantio TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    quantidade INTEGER NOT NULL
                )
            ''')

    def cadastrarPlanta(self, nome, data_plantio, tipo, quantidade):
        with self.conn:
            self.conn.execute('''
                INSERT INTO plantas (nome, data_plantio, tipo, quantidade)
                VALUES (?, ?, ?, ?)
            ''', (nome, data_plantio, tipo, quantidade))
            print("Planta cadastrada!")

    def consultarPlantas(self):
        plantas = self.conn.execute('SELECT * FROM plantas').fetchall()
        if not plantas:
            print("Nenhuma planta cadastrada.")
            return
        for planta in plantas:
            print(f"ID: {planta[0]}, Nome: {planta[1]}, Data de Plantio: {planta[2]}, Tipo: {planta[3]}, Quantidade: {planta[4]}")

    def deletarPlanta(self, planta_id):
        with self.conn:
            cursor = self.conn.execute('DELETE FROM plantas WHERE id = ?', (planta_id,))
            if cursor.rowcount > 0:
                print("Planta deletada!")
            else:
                print("Planta não encontrada.")

    def atualizarPlanta(self, planta_id, nome=None, data_plantio=None, tipo=None, quantidade=None):
        updates = []
        params = []

        if nome:
            updates.append("nome = ?")
            params.append(nome)
        if data_plantio:
            updates.append("data_plantio = ?")
            params.append(data_plantio)
        if tipo:
            updates.append("tipo = ?")
            params.append(tipo)
        if quantidade is not None:
            updates.append("quantidade = ?")
            params.append(quantidade)

        params.append(planta_id)

        if updates:
            with self.conn:
                self.conn.execute(f'''
                    UPDATE plantas SET {', '.join(updates)} WHERE id = ?
                ''', params)
            print("Planta atualizada!")
        else:
            print("Nenhum dado para atualizar.")

    def consultarPlantaIndividual(self, planta_id):
        planta = self.conn.execute('SELECT * FROM plantas WHERE id = ?', (planta_id,)).fetchone()
        if planta:
            print(f"ID: {planta[0]}, Nome: {planta[1]}, Data de Plantio: {planta[2]}, Tipo: {planta[3]}, Quantidade: {planta[4]}")
        else:
            print("Planta não encontrada.")

    def close(self):
        self.conn.close()

