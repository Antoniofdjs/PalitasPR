-- DELETE USER REASSING OWNERSHIPS TO ROOT user
REASSIGN OWNED BY demo_dev TO postgres;
DROP OWNED BY demo_dev;
DROP role demo_dev;
