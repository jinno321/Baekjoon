package goWeb.Communication.Repository;

import goWeb.Communication.Domain.User;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;

import lombok.Getter;
import lombok.Setter;
import org.springframework.stereotype.Repository;

@Repository
@Getter @Setter
public class JpaUserRepository implements UserRepository{

    @PersistenceContext
    private final EntityManager em;

    public JpaUserRepository(EntityManager em){
        this.em = em;
    }


    @Override
    public User createUser() {
        return null;
    }
}
