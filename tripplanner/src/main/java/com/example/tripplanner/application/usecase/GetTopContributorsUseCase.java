package com.example.tripplanner.application.usecase;

import com.example.tripplanner.application.dto.ContributorResponse;
import com.example.tripplanner.infrastructure.persistence.JpaSharedContentRepository;
import com.example.tripplanner.infrastructure.persistence.UserEntity;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class GetTopContributorsUseCase {
    private final JpaSharedContentRepository repository;

    @Transactional(readOnly = true)
    public List<ContributorResponse> execute(int limit) {
        List<Object[]> results = repository.findTopContributors(PageRequest.of(0, limit));
        
        return results.stream().map(result -> {
            UserEntity user = (UserEntity) result[0];
            long count = (long) result[1];
            
            return ContributorResponse.builder()
                    .userId(user.getId())
                    .name(user.getName())
                    .email(user.getEmail())
                    .contributionCount(count)
                    .totalImpact(count * 100) // Placeholder logic for impact
                    .build();
        }).collect(Collectors.toList());
    }
}
