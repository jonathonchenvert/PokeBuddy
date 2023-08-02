# Requirements

* Docker installed

# Getting Started

1. Run the `util/generate_secret_key.py` file to generate a secret key that Django can use.
2. Run `make build` to build the containers (Python and PostgreSQL).
3. Run `make start` to start the containers.
4. Run `make migrations` to create the migration scripts needed (if new migrations need to be applied).
5. Run `make migrate` to migrate the DB updates and apply them to the PostgreSQL DB container.
6. Run `make stop` to stop services.

# Disclaimers

Pokémon © 2002-2019 Pokémon. © 1995-2019 Nintendo/Creatures Inc./GAME FREAK inc. TM, ® and Pokémon character names are trademarks of Nintendo.
No copyright or trademark infringement is intended in using Pokémon content on PokeBuddy.