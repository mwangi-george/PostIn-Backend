from fastapi import HTTPException, status, Response
import time


class RateLimiter:
    count = 0
    start_time = time.time()
    reset_interval = 10
    request_limit = 5

    def rate_limit(self, response: Response) -> Response:
        if time.time() > self.start_time + self.reset_interval:
            self.start_time = time.time()
            self.count = 0

        if self.count >= self.request_limit:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail={
                    "error": "Request limit reached",
                    "time out": round(self.start_time + self.reset_interval - time.time(), 2) + 0.01

                }
            )
        self.count += 1
        response.headers["X-RateLimit-Limit"] = f"{self.count}: {self.request_limit}"
        return response
