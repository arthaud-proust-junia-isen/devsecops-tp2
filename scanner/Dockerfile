# Scanner SonarQube natif arm64 : l'image officielle n'existe qu'en amd64,
# et son analyseur JS plante sous émulation.
# SonarQube 26.x exige Java 21 pour le moteur d'analyse
FROM docker.io/library/amazoncorretto:21-alpine
RUN apk add --no-cache nodejs npm git
ENV SONAR_SCANNER_VERSION=8.4.0.16527
# zip générique, sans JRE embarqué (celui des zips -linux est x86_64)
RUN wget -O /tmp/sonar-scanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip && \
    unzip -q /tmp/sonar-scanner.zip -d /opt && \
    rm /tmp/sonar-scanner.zip && \
    mv /opt/sonar-scanner-${SONAR_SCANNER_VERSION} /opt/sonar-scanner && \
    # le JRE que le serveur proposerait est compilé pour glibc, pas pour Alpine
    echo "sonar.scanner.skipJreProvisioning=true" >> /opt/sonar-scanner/conf/sonar-scanner.properties
ENV PATH="/opt/sonar-scanner/bin:${PATH}"
ENTRYPOINT ["sonar-scanner"]
