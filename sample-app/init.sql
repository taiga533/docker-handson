-- mysqlでユーザーテーブルを作成する
USE test;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- testユーザーにselect, insert, delete, update権限を付与する
GRANT SELECT, INSERT, DELETE, UPDATE ON test.* TO 'test'@'%';

-- test.usersにサンプルデータをbulk insertする
INSERT INTO test.users (name, email) VALUES
('yamada.tarou', 'user1@example.com'),
('yamada.hanako', 'user2@example.com'),
('yamada.takashi', 'user3@example.com');

commit;