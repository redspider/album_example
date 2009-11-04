CREATE TABLE album_permissions (
    album INT REFERENCES album(id),
    group TEXT REFERENCES group(qname),
    permission TEXT REFERENCES permissions(qname)
);

CREATE UNIQUE INDEX album_permissions_pk ON album_permissions (album, group, permission);

CREATE TABLE album (
    id SERIAL PRIMARY KEY,
    created TIMESTAMP,
    name TEXT,
    public BOOLEAN,
    owner TEXT REFERENCES account(username)
);

CREATE FUNCTION add_album(actor TEXT, v_name TEXT, v_public BOOLEAN, v_owner TEXT) RETURNS INT AS
$$
BEGIN
    INSERT INTO album (created, name, public, owner) VALUES (V_NOW(), v_name, v_public, v_owner);
    INSERT INTO album_permissions (currval("album_id_seq"), "guest", "view");
    PERFORM log(actor, "add_album", album);
    RETURN currval("album_id_seq");
END;
$$
LANGUAGE plpgsql;
