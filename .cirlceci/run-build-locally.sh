curl --user ${CIRCLE_TOKEN}: \
    --request POST \
    --form revision=${COMMIT_HASH}\
    --form config=@config.yml \
    --form notify=false \
        https://circleci.com/api/v1.1/project/github/peakshift/ethereum-address-listener/tree/${BRANCH_NAME}