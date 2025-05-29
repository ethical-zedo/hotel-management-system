-- Hotels
INSERT INTO Hotel VALUES (1, 'Paris', 'France', 75001);
INSERT INTO Hotel VALUES (2, 'Lyon', 'France', 69002);

-- Clients
INSERT INTO Client VALUES (1, '12 Rue de Paris', 'Paris', 75001, 'jean.dupont@email.fr', '0612345678', 'Jean Dupont');
INSERT INTO Client VALUES (2, '5 Avenue Victor Hugo', 'Lyon', 69002, 'marie.leroy@email.fr', '0623456789', 'Marie Leroy');
INSERT INTO Client VALUES (3, '8 Boulevard Saint-Michel', 'Marseille', 13005, 'paul.moreau@email.fr', '0634567890', 'Paul Moreau');
INSERT INTO Client VALUES (4, '27 Rue Nationale', 'Lille', 59800, 'lucie.martin@email.fr', '0645678901', 'Lucie Martin');
INSERT INTO Client VALUES (5, '3 Rue des Fleurs', 'Nice', 06000, 'emma.giraud@email.fr', '0656789012', 'Emma Giraud');

-- Prestations
INSERT INTO Prestation VALUES (1, 15, 'Petit-déjeuner');
INSERT INTO Prestation VALUES (2, 30, 'Navette aéroport');
INSERT INTO Prestation VALUES (3, 0, 'Wi-Fi gratuit');
INSERT INTO Prestation VALUES (4, 50, 'Spa et bien-être');
INSERT INTO Prestation VALUES (5, 20, 'Parking sécurisé');

-- Types de chambre
INSERT INTO TypeChambre VALUES (1, 'Simple', 80);
INSERT INTO TypeChambre VALUES (2, 'Double', 120);

-- Chambres
INSERT INTO Chambre VALUES (1, 201, 2, 0, 1, 1);
INSERT INTO Chambre VALUES (2, 502, 5, 1, 1, 2);
INSERT INTO Chambre VALUES (3, 305, 3, 0, 2, 1);
INSERT INTO Chambre VALUES (4, 410, 4, 0, 2, 2);
INSERT INTO Chambre VALUES (5, 104, 1, 1, 2, 2);
INSERT INTO Chambre VALUES (6, 202, 2, 0, 1, 1);
INSERT INTO Chambre VALUES (7, 307, 3, 1, 1, 2);
INSERT INTO Chambre VALUES (8, 101, 1, 0, 1, 1);

-- Réservations
INSERT INTO Reservation VALUES (1, '2025-06-15', '2025-06-18', 1, 1);
INSERT INTO Reservation VALUES (2, '2025-07-01', '2025-07-05', 2, 2);
INSERT INTO Reservation VALUES (3, '2025-08-10', '2025-08-14', 3, 3);
INSERT INTO Reservation VALUES (4, '2025-09-05', '2025-09-07', 4, 4);
INSERT INTO Reservation VALUES (5, '2025-09-20', '2025-09-25', 5, 5);
INSERT INTO Reservation VALUES (7, '2025-11-12', '2025-11-14', 2, 6);
INSERT INTO Reservation VALUES (9, '2026-01-15', '2026-01-18', 4, 7);
INSERT INTO Reservation VALUES (10, '2026-02-01', '2026-02-05', 2, 8);

-- Evaluations
INSERT INTO Evaluation VALUES (1, '2025-06-15', 5, 'Excellent séjour, personnel très accueillant.', 1);
INSERT INTO Evaluation VALUES (2, '2025-07-01', 4, 'Chambre propre, bon rapport qualité/prix.', 2);
INSERT INTO Evaluation VALUES (3, '2025-08-10', 3, 'Séjour correct mais bruyant la nuit.', 3);
INSERT INTO Evaluation VALUES (4, '2025-09-05', 5, 'Service impeccable, je recommande.', 4);
INSERT INTO Evaluation VALUES (5, '2025-09-20', 4, 'Très bon petit-déjeuner, hôtel bien situé.', 5);
