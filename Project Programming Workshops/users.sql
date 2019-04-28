-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 24 Kwi 2018, 20:06
-- Wersja serwera: 10.1.31-MariaDB
-- Wersja PHP: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `forum`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `user` text COLLATE utf8_polish_ci NOT NULL,
  `password` text COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `users`
--

INSERT INTO `users` (`id`, `user`, `password`) VALUES
(1, 'adam', 'qwerty123'),
(2, 'asdf123', '$2y$10$YK9qnyWEi9oGRiikzUHf2exToTEUuyicfgLXwXXFKVNQUExLzgX/6'),
(3, 'qwer123', '$2y$10$w5KiTsga6vSWMQkQYPFoH.BkMZPgljhsEQgpIMd1MU.dkY88j5Wtq'),
(4, 'qwe123', '$2y$10$mf2sEDe2deVCqUkg6.QcKeJlYme/S0cq2ume2BzqnrmSMSdbt75du'),
(5, 'zxc123', '$2y$10$hXoFfs8f4hNWpMywFl6UZ.MALHWU1mE4e/14ihLb6U1vnZMXKc5CW'),
(6, 'qaz123', '$2y$10$nr8CW7xfkfdC/rBsTUuhPuLV.no/7cP9JXyPapnYbsTAMHn3Z8u8G'),
(7, 'sad123', '$2y$10$X5YUqsXhPqVWW38XdjcgxeOly.9ICInxza5jvn1awCd02f7kVBs5a'),
(8, 'edc123', '$2y$10$9yQQxRh525e/9d0LaZ5ZguuujIjXyqsxHo4soRtZvYnde4td8rDgO');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
