%% Basics of Probability - Coin Flip

% Set the random seed
rng(49);

% Set the probability threshold
p = 0.5;

% Set the number of trails
n = 10000;

% Initialise an array with the probabilities over time (isHeads, isTails)
P = zeros([n,2]);


%% Loop through each trial - counting Heads or Tails
for i = 1:n

    p_i = rand(1);

    % If the current probability is below the threshold, it is a Heads
    if p_i <= p

        % Set the 1st column of pT as 1 to denote Heads
        P(i,1) = 1;

    else

        % Set the 2nd column of pT as 1 to denote Tails
        P(i,2) = 1;

    end

end

%% Probability calculations

% Cumulative sum of Heads
csH = cumsum(P(:,1));

% Cumulative sum of Heads
csT = cumsum(P(:,2));

% Intitialise heads and tails probability arrays
pH = zeros([n,1]);
pT = zeros([n,1]);

% Loop to get probabiltiies
for i = 1:n

    pH(i) = csH(i) / i;
    pT(i) = csT(i) / i;


end


%% Plotting
figure("Name", 'Coin Flip Probability')
hold on

% Create a flat line at p
pLine = [0, p; n, p];

% Plot the line
plot(pLine(:,1), pLine(:,2), 'Color', 'r', 'LineStyle','--', 'LineWidth',2);

% Plot the probabilities over time
plot((1:n)', pH, 'Color', 'b', 'LineWidth',2);